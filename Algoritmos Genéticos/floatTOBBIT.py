L = 4 * 8 #size of chromossome in bits

import struct
import random
import math
#import matplotlib.pyplot as plot
#import numpy as np

def floatToBits(f):
        s = struct.pack('>f', f)
        return struct.unpack('>L', s)[0]

def bitsToFloat(b):
        s = struct.pack('>L', b)
        return struct.unpack('>f', s)[0]

#exemplo 1.23 -> '0010111100'

def get_bits(x):
        x = floatToBits(x)
        N = 4 * 8
        bits = ''
        for bit in range(N):
                b = x & (2**bit)
                bits += '1' if b > 0 else '0'
        return bits

#exemplo '00010111100' -> 1.23

def get_float(bits):
        x = 0
        assert(len(bits) == L)
        for i, bit in enumerate(bits):
                bit = int(bit)  #0 or 1
                x += bit * (2**i)
        return bitsToFloat(x)


print(get_bits(0.8319408673398835))


#Peopel =['01101101001101100001101111111100', '00001000000010011100100000000010', '11101111000111000001000000000010', '00000100001101100100001000000010', '00111100010101100100000111111100', '11001010000000001010010111111100', '01110111010001110011100001111100', '01111000110011100110001000000010', '11011000111011000001000111111100', '10000100111101011000110011111100']

#nova =  ['01101101001101101010010111111100', '11001010000000000001101111111100', '01101101001101101010010111111100', '11001010000000000001101111111100', '01101101001101101010010111111100', '11001010000000000001101111111100', '01101101001101101010010111111100', '11001010000000000001101111111100', '01101101001101101010010111111100', '11001010000000000001101111111100']
