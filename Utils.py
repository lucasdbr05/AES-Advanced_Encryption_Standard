import numpy as np 
import base64

def convert_string_to_binary(data: str) -> int:
    data = ''.join(format(ord(i), '08b') for i in data)
    return int(data, base=2)
    
def padding(text):
    return text + ((len(text)) % 2) * " "

def format_bin (x: str) -> str:
    return bin(x)[2:].zfill(16)

def parse_str_to_int(data: str) -> np.uint16:
    return (ord(data[0])<<8) + (ord(data[1]))
    

def int_to_nibble_matrix(value: np.uint16) -> list[list[int]]:
    aux = [0, 0, 0, 0]
    for i in range(4):
        aux[i] = value & 0xF
        value >>= 4

    return [[aux[3], aux[1]] , [aux[2],aux[0]]]

def nibble_matrix_to_int(matrix: list[list[int]]) ->  np.int16:
    return (matrix[0][0] << 12) + (matrix[1][0] << 8) + (matrix[0][1] << 4) + matrix[1][1]

def parse_int_to_string(data: int)-> str:
    string = ""
    while (data> 0):
        string = chr(data & 0xFF) + string 
        data = data >> 8
    while(len(string) < 2):
        string = chr(0) + string
    return string

def to_base64(data: int) -> str:
    return base64.b64encode(str(data).encode()).decode()
