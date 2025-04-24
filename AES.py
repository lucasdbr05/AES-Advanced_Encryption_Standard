from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from Crypto.Util import Counter 

class OperationModes:
    def __init__(self, key: str) -> None:
        self.key = key.encode()

    def encrypt(self, data: str) -> None:
        data = data.encode()
        print(self.__encrypt_in_ECB(data))
        print(self.__encrypt_in_CBC(data))
        print(self.__encrypt_in_CFB(data))
        print(self.__encrypt_in_OFB(data))
        print(self.__encrypt_in_CTR(data))

    def __encrypt_in_ECB(self, data: bytes) -> bytes:
        ECB_cipher =  AES.new(self.key, AES.MODE_ECB)
        data = pad(data, AES.block_size)
        return ECB_cipher.encrypt(data)
    
    def __encrypt_in_CBC(self, data: bytes) -> bytes:
        iv = get_random_bytes(AES.block_size)
        CBC_cipher = AES.new(self.key, AES.MODE_CBC, iv = iv)
        data = pad(data, AES.block_size)
        return CBC_cipher.encrypt(data)

    def __encrypt_in_CFB(self, data: bytes) -> bytes:
        iv = get_random_bytes(AES.block_size)
        CFB_cipher = AES.new(self.key, AES.MODE_CFB, iv = iv)
        data = pad(data, AES.block_size)
        return CFB_cipher.encrypt(data)

    def __encrypt_in_OFB(self, data: bytes) -> bytes:
        iv = get_random_bytes(AES.block_size)
        OFB_cipher = AES.new(self.key, AES.MODE_OFB, iv = iv)
        return OFB_cipher.encrypt(data)

    def __encrypt_in_CTR(self, data: bytes) -> bytes:
        counter = Counter.new(nbits=128)
        CTR_cipher = AES.new(self.key, AES.MODE_CTR, counter = counter)
        return CTR_cipher.encrypt(data)
    
  

    
