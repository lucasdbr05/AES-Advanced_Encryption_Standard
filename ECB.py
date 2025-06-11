from S_AES import S_AES
import numpy as np
from Utils import format_bin, padding
from Logger import Logger


def encrypt_saes_ecb(text: str, key: np.int16) -> str:
    """
        Encrypt a given text using the Simplified AES (S-AES) algorithm in ECB mode.
        Args:
            text (str): The input text to be decrypted. It should be a string of characters.
            key (np.int16): The encryption key used for decryption, represented as a 16-bit integer.
        Returns:
            str: the ciphertext resulting in ECB mode encryptation
    """
    # Initialize the S-AES instance with the provided key
    s_aes = S_AES(key)
    # Pad the input text to ensure it fits the block size
    text = padding(text)

    blocks = []
    # Process the text in blocks of 2 characters
    for i in range(0, len(text), 2):
        block = text[i: i+2]
        # Encrypt each block using S-AES
        data = s_aes.encrypt(block)
        blocks.append(data)

    # Log the encrypted data for each block
    for i in range(len(blocks)):
        Logger.print_saes_block(blocks[i], f"Data for block {i+1}")        

    # Combine all encrypted blocks into a single binary string
    return "".join(format_bin(block) for block in blocks)


def decrypt_saes_ecb(text: str, key: np.int16) -> str:
    """
    Decrypts a given text using the Simplified AES (S-AES) algorithm in ECB mode.
    Args:
        text (str): The input text to be decrypted. It should be a string of characters.
        key (np.int16): The encryption key used for decryption, represented as a 16-bit integer.
    Returns:
        str: the original plaintext resulting in ECB mode decryptation 
    """
    # Initialize the S-AES instance with the provided key
    s_aes = S_AES(key)
    # Pad the input text to ensure it fits the block size
    text = padding(text)

    blocks = []
    # Process the text in blocks of 2 characters
    for i in range(0, len(text), 2):
        block = text[i: i+2]
        # Decrypt each block using S-AES
        data = s_aes.decrypt(block)
        blocks.append(data) 

    # Log the decrypted data for each block
    for i in range(len(blocks)):
        Logger.print_saes_block(blocks[i], f"Data for block {i+1}")        

    # Combine all decrypted blocks into a single binary string
    return "".join(format_bin(block) for block in blocks)


def identic_blocs_comparison():
    message_1 = "ababacaba"
    message_2 = "abacacaba"
    key = 0X4af5
    Logger.print_string(f"Blocks to be compared:\nmessage 1: {message_1}\nmessage 2: {message_2}")
    cipher_1 = encrypt_saes_ecb(message_1, key)
    cipher_2 = encrypt_saes_ecb(message_2, key)
    Logger.print_string("Messages comparisson")
    Logger.print_saes_block(int(cipher_1, base=2), "Message 1 encrypted")
    Logger.print_saes_block(int(cipher_2, base=2), "Message 2 encrypted")
