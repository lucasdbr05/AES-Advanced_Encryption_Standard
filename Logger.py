from pprint import pprint
import time 
from Utils import parse_int_to_string, to_base64, int_to_nibble_matrix
class Logger:
    @staticmethod
    def start(is_from_user:bool) -> None:
        print("Options:")
        print()
        print(f"T: change input origin for {"user" if not is_from_user else "default"} inputs")
        print("0: Stop")
        print("1A: encrypt using S-AES")
        print("1B: decrypt using S-AES")
        print("2A: S-AES encryptation with ECB operation mode")
        print("2B: S-AES decryptation with ECB operation mode")
        print("3: AES in differents operations mode")


    @staticmethod
    def print_string(data: str) -> None:
        print(data)

    @staticmethod
    def print_saes_block(data: int, title: str = None) -> None:
        if(title):
            print(title)

        pprint({
            "binary": bin(data)[2:].zfill(16),
            "hexadecimal": hex(data)[2:].zfill(4),
            "base64": to_base64(data),
            "string": parse_int_to_string(data)
        })
        print()

    @staticmethod
    def print_aes_data(operation_mode: str, data: str) -> None:
        print(f"Operation Mode : {operation_mode}")
        data["base64"] = to_base64(data["binary"])
        data["execution time"] = f"{data['execution time'] * 1000} miliseconds"    
        pprint(data)
        print()

    @staticmethod
    def print_saes_block_with_nibbles_matrix(data: int, title: str = None) -> None:
        if(title):
            print(title)

        pprint({
            "binary": bin(data)[2:].zfill(16),
            "hexadecimal": hex(data)[2:].zfill(4),
            "base64": to_base64(data),
            "nibbles matrix": int_to_nibble_matrix(data),
            "string": parse_int_to_string(data)
        })
        print()