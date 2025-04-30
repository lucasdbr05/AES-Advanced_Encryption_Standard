from pprint import pprint
import time 
from Utils import parse_int_to_string, to_base64
class Logger:
    @staticmethod
    def start() -> None:
        print("Options:")
        print()
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