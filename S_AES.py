import numpy as np

class S_AES():
    def __init__(self, key: int) -> None:
        self._key = key
        self._S_box =  [ 0b1001, 0b0100, 0b1010, 0b1011, 0b1101, 0b0001, 0b1000, 0b0101, 0b0110, 0b0010, 0b0000, 0b0011, 0b1100, 0b1110, 0b1111, 0b0111, ]
        self._S_box_inv = [ 0b1010, 0b0101, 0b1001, 0b1011, 0b0001, 0b0111, 0b1000, 0b1111, 0b0110, 0b0000, 0b0010, 0b0011, 0b1100, 0b0100, 0b1101, 0b1110, ]
        
        self._k0, self._k1, self._k2 =  self._expand_key(key)

    def _substitute_nibbles(self, value: np.uint8) -> np.uint8:
            N0 = value & 0b1111
            N1 = (value >> 4) & 0b1111

            return ((self._S_box[N1] << 4) + self._S_box[N0])
    
    def _rotate_niblles(self, value: np.uint8) -> np.uint8:
        return ((value >> 4) & 0xF) + ((value << 4) & 0xFF)

    def _G(self, value: np.uint8, round: int) -> np.uint8:
        RCON = [0, 0b10000000, 0b00110000]
        return RCON[round] ^ self._substitute_nibbles(self._rotate_niblles(value))
    
    def _expand_key(self, key: np.uint16) -> tuple[np.uint16]:
        build_key = lambda x0, x1: (x0<<8) + x1  
        
        # Before rounds 
        W0 = (key >> 8) & 0xFF
        W1 = (key) & 0xFF
        K0 = build_key(W0, W1)

        # First round key
        W2 = W0 ^ self._G(W1, 1)
        W3 = W2 ^ W1
        K1 = build_key(W2, W3)
        
        # Second round key
        W4 = W2 ^ self._G(W3, 2)
        W5 = W4 ^ W3
        K2 = build_key(W4, W5)

        return (K0, K1, K2)

    def _add_round_key(data: np.uint16, key: np.uint16):
        return data ^ key 





