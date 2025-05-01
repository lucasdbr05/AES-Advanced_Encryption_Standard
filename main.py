from os import system
from Logger import Logger
from S_AES import S_AES
from ECB import encrypt_saes_ecb, decrypt_saes_ecb
from AES import AES_OperationModes

def do_command(data: str) -> None:
    if (data == "1A"):
        Logger.print_string("Type S-AES key (hexadecimal):")
        key = int(input(), base=16)
        Logger.print_string("Type data to be encrypted (data must have 2 chars -> 16 bits):")
        text = input()
        s_aes = S_AES(key)
        Logger.print_saes_block(s_aes.encrypt(text))
    elif (data == "1B"):
        Logger.print_string("Type S-AES key (hexadecimal):")
        key = int(input(), base=16)
        Logger.print_string("Type data to be decrypted (data must have 2 chars -> 16 bits):")
        text = input()
        s_aes = S_AES(key)
        Logger.print_saes_block(s_aes.decrypt(text))
    elif (data == "2A"):
        Logger.print_string("Type S-AES key (hexadecimal):")
        key = int(input(), base=16)
        Logger.print_string("Type data to be encrypted:")
        text = input()
        text = encrypt_saes_ecb(text, key)
        Logger.print_saes_block(int(text, base=2), "Final ECB operation message encryption")
    elif (data == "2B"):
        Logger.print_string("Type S-AES key (hexadecimal):")
        key = int(input(), base=16)
        Logger.print_string("Type data to be decrypted:")
        text = input()
        text = decrypt_saes_ecb(text, key)
        Logger.print_saes_block(int(text, base=2), "Final ECB operation message decryption")
    elif (data == "3"):
        key = "Fluminense F.C. "
        text = "FLUMINENSEGRANDE"*10
        Logger.print_string(f"Key: {key}\nPlainText: {text}\n(key and text are fixed)\n")
        operation_modes = AES_OperationModes(key)
        operation_modes.encrypt(text)
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
