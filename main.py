from os import system
from Logger import Logger
from S_AES import S_AES
from ECB import encrypt_saes_ecb
from AES import AES_OperationModes


def do_command(data: str) -> None:
    if (data == "1A"):
        Logger.print_string("Type S-AES key (hexadecimal):")
        key = int(input(), base=16)
        Logger.print_string("Type data to be encrypted:")
        text = input()
        s_aes = S_AES(key)
        Logger.print_saes_block(s_aes.encrypt(text))
    elif (data == "1B"):
        Logger.print_string("Type S-AES key (hexadecimal):")
        key = int(input(), base=16)
        Logger.print_string("Type data to be decrypted:")
        text = input()
        s_aes = S_AES(key)
        Logger.print_saes_block(s_aes.encrypt(text))
    elif (data == "2A"):
        Logger.print_string("Type S-AES key (hexadecimal):")
        key = int(input(), base=16)
        Logger.print_string("Type data to be encrypted:")
        text = input()
        blocks = encrypt_saes_ecb(text, key)
        for i in range(len(blocks)):
            Logger.print_saes_block(blocks[i], f"Data for block {i+1}")
    elif (data == "2B"):
        Logger.print_string("Type S-AES key (hexadecimal):")
        key = int(input(), base=16)
        text = input()
        Logger.print_string("Type data to be decrypted:")
        blocks = encrypt_saes_ecb(text, key)
        for i in range(len(blocks)):
            Logger.print_saes_block(blocks[i], f"Data for block {i+1}")
    elif (data == "3"):
        operation_modes = AES_OperationModes("Fluminense F.C. ")
        operation_modes.encrypt(1000*"FLUMINENSEGRANDEFLUMINENSEGRANDEFLUMINENSEGRANDEFLUMINENSEGRANDEFLUMINENSEGRANDE")
    else:
        Logger.print_string("Command not found :(")
    
    Logger.print_string("Press y to continue")
    while(not input()): continue
    

if __name__ == "__main__":
    while (True):
        Logger.start()
        option = input()
        system("clear")

        if(option== '0'):
            break
        
        do_command(option)
        system("clear")
