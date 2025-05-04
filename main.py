from os import system
from Logger import Logger
from S_AES import S_AES
from ECB import encrypt_saes_ecb, decrypt_saes_ecb
from AES import AES_OperationModes

def get_input(from_user: bool, file_path: str = None) -> str:
    if(from_user):
        return input()
    else:
        content = open(file_path, 'r', encoding="utf-8").read()
        print(content)
        return content

def do_command(data: str, from_user: bool) -> None:
    if (data == "1A"):
        Logger.print_string("Type S-AES key (hexadecimal):")
        key = int(get_input(from_user, "inputs/1_a_key.txt"), base=16)
        Logger.print_string("Type data to be encrypted (data must have 2 chars -> 16 bits):")
        text = get_input(from_user, "inputs/1_a_text.txt")
        s_aes = S_AES(key)
        Logger.print_saes_block(s_aes.encrypt(text), "S-AES encryption result")
    elif (data == "1B"):
        Logger.print_string("Type S-AES key (hexadecimal):")
        key = int(get_input(from_user, "inputs/1_b_key.txt"), base=16)
        Logger.print_string("Type data to be decrypted (data must have 2 chars -> 16 bits):")
        text = get_input(from_user, "inputs/1_b_text.txt")
        s_aes = S_AES(key)
        Logger.print_saes_block(s_aes.decrypt(text), "S-AES decryption result")
    elif (data == "2A"):
        Logger.print_string("Type S-AES key (hexadecimal):")
        key = int(get_input(from_user, "inputs/2_a_key.txt"), base=16)
        Logger.print_string("Type data to be encrypted:")
        text = get_input(from_user, "inputs/2_a_text.txt")
        text = encrypt_saes_ecb(text, key)
        Logger.print_saes_block(int(text, base=2), "Final ECB operation message encryption")
    elif (data == "2B"):
        Logger.print_string("Type S-AES key (hexadecimal):")
        key = int(get_input(from_user, "inputs/2_b_key.txt"), base=16)
        Logger.print_string("Type data to be decrypted:")
        text = get_input(from_user, "inputs/2_b_text.txt")
        text = decrypt_saes_ecb(text, key)
        Logger.print_saes_block(int(text, base=2), "Final ECB operation message decryption")
    elif (data == "3"):
        Logger.print_string("Type AES key (string 16 bytes):")
        key = get_input(from_user, "inputs/3_key.txt")
        Logger.print_string("Type data to be decrypted:")
        text = get_input(from_user, "inputs/3_text.txt")
        operation_modes = AES_OperationModes(key)
        operation_modes.encrypt(text)
    else:
        Logger.print_string("Command not found :(")
    
    Logger.print_string("Press y to continue")
    while(not input()): continue
    

if __name__ == "__main__":
    inputs_from_user = False
    while (True):
        Logger.start(inputs_from_user)
        option = input()
        system("clear")

        if(option=="T"):
            inputs_from_user = not inputs_from_user
            continue
        if(option== '0'):
            break
        
        do_command(option, inputs_from_user)
        system("clear")
