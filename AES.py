from Crypto.Cipher import AES

class OperationModes:
    def __init__(self, key: str) -> None:
        self.key = b"Fluminense F.C. "

    def encrypt(self, data: str) -> str:
        data = data.encode()
        data = data[0:16]
        print(self.__encrypt_in_ECB(data))
        print(self.__encrypt_in_CBC(data))
        print(self.__encrypt_in_CFB(data))
        print(self.__encrypt_in_OFB(data))
        print(self.__encrypt_in_CTR(data))


    def __encrypt_in_ECB(self, data: str):
        return AES.new(self.key, AES.MODE_ECB).encrypt(data)
    
    def __encrypt_in_CBC(self, data: str):
        return AES.new(self.key, AES.MODE_CBC).encrypt(data)

    def __encrypt_in_CFB(self, data: str):
        return AES.new(self.key, AES.MODE_CFB).encrypt(data)

    def __encrypt_in_OFB(self, data: str):
        return AES.new(self.key, AES.MODE_OFB).encrypt(data)

    def __encrypt_in_CTR(self, data: str):
        return AES.new(self.key, AES.MODE_CTR).encrypt(data)
    
  

    
