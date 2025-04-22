from pprint import pprint
import base64

def parse_int_to_string(data: int)-> str:
    return chr(data>>8 & 0xFF) + chr(data & 0xFF)

class Logger:
    @staticmethod
    def start() -> None:
        print("Options:")
        print()
        print("0: Stop")
        print("1A: encrypt using S-AES")
        print("1B: decrypt using S-AES")
        print("2: S-AES encryptation with ECB operation mode")
        print("2: S-AES decryptation with ECB operation mode")
        print("3: AES in differents operations mode")


    @staticmethod
    def print_string(data: str) -> None:
        print(data)

    @staticmethod
    def print_block(data: int, title: str = None) -> None:
        if(title):
            print(title)

        pprint({
            "binary": bin(data)[2:].zfill(16),
            "hexadecimal": hex(data)[2:].zfill(4),
            "base64": base64.b64encode(str(data).encode()).decode(),
            "string": parse_int_to_string(data)
        })
        print()

    @staticmethod
    def print_stream(data: list[int]) -> None:
        pass