from S_AES import S_AES
import numpy as np

def convert_string_to_binary(data: str) -> int:
    data = ''.join(format(ord(i), '08b') for i in data)
    return int(data, base=2)
    
def padding(text):
    return text + ((len(text)) % 2) * " "

def format_bin (x: str) -> str:
    return bin(x)[2:].zfill(16)

def encrypt_saes_ecb(text: str, key: np.int16) -> str:
        s_aes = S_AES(key)
        text = padding(text)

        result = []
        for i in range(0, len(text), 2):
            block = convert_string_to_binary(text[i: i+2])
            data = s_aes.encrypt(block)
            result.append(data)

        binary = ''.join(format_bin(data) for data in result)
        return binary

def decrypt_saes_ecb(text: str, key: np.int16) -> str:
        s_aes = S_AES(key)
        text = padding(text)

        result = []
        for i in range(0, len(text), 2):
            block = convert_string_to_binary(text[i: i+2])
            data = s_aes.encrypt(block)
            result.append(data)

        binary =  ''.join(format_bin(data) for data in result)
        return binary
