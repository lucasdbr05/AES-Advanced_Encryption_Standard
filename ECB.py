from S_AES import S_AES
import numpy as np
from Utils import convert_string_to_binary, format_bin, padding
from Logger import Logger

def encrypt_saes_ecb(text: str, key: np.int16) -> str:
        s_aes = S_AES(key)
        text = padding(text)

        blocks = []
        for i in range(0, len(text), 2):
            block = text[i: i+2]
            data = s_aes.encrypt(block)
            blocks.append(data)

        for i in range(len(blocks)):
            Logger.print_saes_block(blocks[i], f"Data for block {i+1}")        
        
        return "".join(format_bin(block) for block in blocks)
        
def decrypt_saes_ecb(text: str, key: np.int16) -> list[int]:
    s_aes = S_AES(key)
    text = padding(text)

    blocks = []
    for i in range(0, len(text), 2):
        block = text[i: i+2]
        data = s_aes.decrypt(block)
        blocks.append(data) 
    return blocks
