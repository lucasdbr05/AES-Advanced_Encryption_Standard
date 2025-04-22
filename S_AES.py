import numpy as np

class S_AES():
    def __init__(self, key: np.uint16) -> None:
        self.__key = key
        self.__S_box =  [ 0b1001, 0b0100, 0b1010, 0b1011, 0b1101, 0b0001, 0b1000, 0b0101, 0b0110, 0b0010, 0b0000, 0b0011, 0b1100, 0b1110, 0b1111, 0b0111, ]
        self.__S_box_inv = [ 0b1010, 0b0101, 0b1001, 0b1011, 0b0001, 0b0111, 0b1000, 0b1111, 0b0110, 0b0000, 0b0010, 0b0011, 0b1100, 0b0100, 0b1101, 0b1110, ]
        
        self.__K0, self.__K1, self.__K2 =  self.__expand_key(key)

    def parse_str_to_int(self, data: str) -> np.uint16:
        return (ord(data[0])<<8) + (ord(data[1]))
    
    def encrypt(self, data: str) -> np.uint16:
        # Parse string to bits
        data = self.parse_str_to_int(data)     

        # Pre-rounds 
        data = self.__add_round_key(data, self.__K0)

        # First Round
        data = self.__substitute_nibbles(data)
        data = self.__shift_rows(data)
        data = self.__mix_columns(data)
        data = self.__add_round_key(data, self.__K1)

        # Second Round 
        data = self.__substitute_nibbles(data)
        data = self.__shift_rows(data)
        data = self.__add_round_key(data, self.__K2)

        return data

    def decrypt(self, data: str) -> np.uint16:
        # Parse string to bits
        data = self.parse_str_to_int(data)     
        

        # Pre-rounds 
        data = self.__add_round_key(data, self.__K2)

        # First Round
        data = self.__shift_rows(data)
        data = self.__inverse_substitute_nibbles(data)
        data = self.__add_round_key(data, self.__K1)
        data = self.__inverse_mix_columns(data)

        # Second Round 
        data = self.__shift_rows(data)
        data = self.__inverse_substitute_nibbles(data)
        data = self.__add_round_key(data, self.__K0)

        return data
                

    def int_to_matrix(self, value: np.uint16) -> list[list[int]]:
        aux = [0, 0, 0, 0]
        for i in range(4):
            aux[i] = value & 0xF
            value >>= 4

        return [[aux[3], aux[1]] , [aux[2],aux[0]]]
    
    def matrix_to_int(self, matrix: list[list[int]]) ->  np.int16:
        return (matrix[0][0] << 12) + (matrix[1][0] << 8) + (matrix[0][1] << 4) + matrix[1][1]

    def __substitute_nibbles_in_key_expansion(self, value: np.uint8) -> np.uint8:
            N0 = value & 0b1111
            N1 = (value >> 4) & 0b1111

            return ((self.__S_box[N1] << 4) + self.__S_box[N0])
    
    def __rotate_nibbles(self, value: np.uint8) -> np.uint8:
        return ((value >> 4) & 0xF) + ((value << 4) & 0xFF)

    def __G(self, value: np.uint8, round: int) -> np.uint8:
        RCON = [0, 0b10000000, 0b00110000]
        return RCON[round] ^ self.__substitute_nibbles_in_key_expansion(self.__rotate_nibbles(value))
    
    def __expand_key(self, key: np.uint16) -> tuple[np.uint16]:
        build_key = lambda x0, x1: (x0<<8) + x1  
        
        # Before rounds 
        W0 = (key >> 8) & 0xFF
        W1 = (key) & 0xFF
        K0 = build_key(W0, W1)

        # First round key
        W2 = W0 ^ self.__G(W1, 1)
        W3 = W2 ^ W1
        K1 = build_key(W2, W3)
        
        # Second round key
        W4 = W2 ^ self.__G(W3, 2)
        W5 = W4 ^ W3
        K2 = build_key(W4, W5)

        return (K0, K1, K2)

    def __add_round_key(self, data: np.uint16, key: np.uint16):
        return data ^ key 

    def __substitute_nibbles(self, value: np.int16) -> np.int16:
        shift = 0
        new_value = 0
        for _ in range(4):
            current_nibble = value & 0xF
            current_nibble = self.__S_box[current_nibble]
            new_value += (current_nibble << shift)
            value >>= 4
            shift += 4 
        return new_value

    def __inverse_substitute_nibbles(self, value: np.int16) -> np.int16:
        shift = 0
        new_value = 0
        for _ in range(4):
            current_nibble = value & 0xF
            current_nibble = self.__S_box_inv[current_nibble]
            new_value += (current_nibble << shift)
            value >>= 4
            shift += 4 
        return new_value
    
    def __shift_rows(self, value: np.int16) -> np.int16:
        m = self.int_to_matrix(value)
        c0 = (m[0][0] << 4) + m[1][1]
        c1 = (m[0][1] << 4) + m[1][0]
        
        return (c0 << 8) + c1

    def __mix_columns(self, value: np.int16) -> np.int16:
        matrix = self.int_to_matrix(value)

        mixed_columns_matrix = [[0, 0], [0, 0]]

        mixed_columns_matrix[0][0] = matrix[0][0] ^ self.__GF_multiplication(4, matrix[1][0])
        mixed_columns_matrix[0][1] = matrix[0][1] ^ self.__GF_multiplication(4, matrix[1][1])
        mixed_columns_matrix[1][0] = matrix[1][0] ^ self.__GF_multiplication(4, matrix[0][0])
        mixed_columns_matrix[1][1] = matrix[1][1] ^ self.__GF_multiplication(4, matrix[0][1])

        return self.matrix_to_int(mixed_columns_matrix)
    
    def __inverse_mix_columns(self, value: np.int16) -> np.int16:
        matrix = self.int_to_matrix(value)

        mixed_columns_matrix = [[0, 0], [0, 0]]

        mixed_columns_matrix[0][0] = self.__GF_multiplication(9, matrix[0][0]) ^ self.__GF_multiplication(2, matrix[1][0])
        mixed_columns_matrix[0][1] = self.__GF_multiplication(9, matrix[0][1]) ^ self.__GF_multiplication(2, matrix[1][1])
        mixed_columns_matrix[1][0] = self.__GF_multiplication(9, matrix[1][0]) ^ self.__GF_multiplication(2, matrix[0][0])
        mixed_columns_matrix[1][1] = self.__GF_multiplication(9, matrix[1][1]) ^ self.__GF_multiplication(2, matrix[0][1])

        return self.matrix_to_int(mixed_columns_matrix)

    def __GF_multiplication(self, x: int, y: int) -> int:
        """Galois field multiplication of x and y in GF(2^4) / x**4 + x + 1
        :param x: First number
        :param y: Second number
        :return: Multiplication of both under GF(2^4)
        """
        result = 0

        x = x & 0x0F
        y = y & 0x0F

        # While both multiplicands are non-zero
        while x and y:
            # If LSB of b is 1
            if y & 1:
                result = result ^ x
            x = x << 1

            # If a overflows beyond 4th bit
            if x & (1 << 4):
                # XOR with irreducible polynomial with high term eliminated (x**4 + x + 1)
                x = x ^ 0b10011
            y = y >> 1


        return result