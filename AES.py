from Logger import Logger
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from Crypto.Util import Counter 
import numpy as np
from math import log
from scipy.special import gammaincc
import time 
from Utils import to_base64

class AES_OperationModes:
    def __init__(self, key: str) -> None:
        self.key = key.encode()

    def encrypt(self, data: str) -> None:
        data = data.encode()
        operation_modes = {
            "ECB": self.__encrypt_in_ECB,
            "CBC": self.__encrypt_in_CBC,
            "CFB": self.__encrypt_in_CFB,
            "OFB": self.__encrypt_in_OFB,
            "CTR": self.__encrypt_in_CTR,
        }
        
        for (operation_mode, fn) in operation_modes.items(): 
            start = time.perf_counter()
            cypher_data = fn(data)
            end = time.perf_counter()
            execution_time = end - start
            aes_data = {
                "binary": cypher_data,
                "execution time": execution_time,
                "entropy": self.approximate_entropy(cypher_data)
            }
            Logger.print_aes_data(operation_mode, aes_data)
            print(" -"*20)
            
    def __encrypt_in_ECB(self, data: bytes) -> bytes:
        # Encrypts the data using AES in ECB (Electronic Codebook) mode.
        # This mode divides the plaintext into blocks and encrypts each block independently.
        ECB_cipher = AES.new(self.key, AES.MODE_ECB)
        data = pad(data, AES.block_size)  # Pads the data to ensure it is a multiple of the block size.
        return ECB_cipher.encrypt(data)
    
    def __encrypt_in_CBC(self, data: bytes) -> bytes:
        # Encrypts the data using AES in CBC (Cipher Block Chaining) mode.
        # This mode uses an initialization vector (IV) and chains the encryption of blocks to improve security.
        iv = get_random_bytes(AES.block_size)  # Generates a random IV for encryption.
        CBC_cipher = AES.new(self.key, AES.MODE_CBC, iv=iv)
        data = pad(data, AES.block_size)  # Pads the data to ensure it is a multiple of the block size.
        return CBC_cipher.encrypt(data)

    def __encrypt_in_CFB(self, data: bytes) -> bytes:
        # Encrypts the data using AES in CFB (Cipher Feedback) mode.
        # This mode allows encryption of data in smaller units than the block size.
        iv = get_random_bytes(AES.block_size)  # Generates a random IV for encryption.
        CFB_cipher = AES.new(self.key, AES.MODE_CFB, iv=iv)
        data = pad(data, AES.block_size)  # Pads the data to ensure it is a multiple of the block size.
        return CFB_cipher.encrypt(data)

    def __encrypt_in_OFB(self, data: bytes) -> bytes:
        # Encrypts the data using AES in OFB (Output Feedback) mode.
        # This mode turns a block cipher into a synchronous stream cipher.
        iv = get_random_bytes(AES.block_size)  # Generates a random IV for encryption.
        OFB_cipher = AES.new(self.key, AES.MODE_OFB, iv=iv)
        return OFB_cipher.encrypt(data)

    def __encrypt_in_CTR(self, data: bytes) -> bytes:
        # Encrypts the data using AES in CTR (Counter) mode.
        # This mode uses a counter value that is incremented for each block, ensuring unique encryption for each block.
        counter = Counter.new(nbits=128)  # Creates a counter object for CTR mode.
        CTR_cipher = AES.new(self.key, AES.MODE_CTR, counter=counter)
        return CTR_cipher.encrypt(data)
        
    def approximate_entropy(self, data: bytes, pattern_length=10) -> float:
        """
        Note that this description is taken from the NIST documentation [1]
        [1] http://csrc.nist.gov/publications/nistpubs/800-22-rev1a/SP800-22rev1a.pdf
        As with the Serial test of Section 2.11, the focus of this test is the frequency of all possible overlapping
        m-bit patterns across the entire sequence. The purpose of the test is to compare the frequency of overlapping
        blocks of two consecutive/adjacent lengths (m and m+1) against the expected result for a random sequence.
        :param bin_data: a binary string
        :param pattern_length: the length of the pattern (m)
        :return: the P value
        """
        bin_data = ''.join(format(byte, '08b') for byte in data)

        n = len(bin_data)
        # Add first m+1 bits to the end
        # NOTE: documentation says m-1 bits but that doesnt make sense, or work.
        bin_data += bin_data[:pattern_length + 1:]

        # Get max length one patterns for m, m-1, m-2
        max_pattern = ''
        for i in range(pattern_length + 2):
            max_pattern += '1'

        # Keep track of each pattern's frequency (how often it appears)
        vobs_one = np.zeros(int(max_pattern[0:pattern_length:], 2) + 1)
        vobs_two = np.zeros(int(max_pattern[0:pattern_length + 1:], 2) + 1)

        for i in range(n):
            # Work out what pattern is observed
            vobs_one[int(bin_data[i:i + pattern_length:], 2)] += 1
            vobs_two[int(bin_data[i:i + pattern_length + 1:], 2)] += 1

        # Calculate the test statistics and p values
        vobs = [vobs_one, vobs_two]
        sums = np.zeros(2)
        for i in range(2):
            for j in range(len(vobs[i])):
                if vobs[i][j] > 0:
                    sums[i] += vobs[i][j] * log(vobs[i][j] / n)
        sums /= n
        ape = sums[0] - sums[1]
        chi_squared = 2.0 * n * (log(2) - ape)
        p_val = gammaincc(pow(2, pattern_length-1), chi_squared/2.0)
        return float(p_val)