
#Algoritmo genético 

L = 4 * 8 #size of chromossome in bits

import struct
import random
import math


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


#size of population
n = 4

people = []

def population():
        for i in range(n):
                p = random.SystemRandom().uniform(0, math.pi)
                if p == math.pi:
                        p = round(p)                             
                else:
                        print(p)
                person = get_bits(p)
                print(person)
                people.append(person)
                
population() #population

print(people) #list of people

fitnessList = []

def calc_fitness():
        for t in range(len(people)):
                people[t] = get_float(people[t])
                fitness   = people[t] + math.sin(32*people[t])
                fitnessList.append(fitness)

calc_fitness()

print(fitnessList) #list of fitness 



