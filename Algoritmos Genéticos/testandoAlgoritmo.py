import random
import math
import struct

L = 4 * 8 #size of chromossome in bits

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

def pop_len():
        p = int(input("digit the number of population:  "))
        if(p%2 != 0):
                print("odd number")
                p = p - 1
                print("changed to even")
                return p
        else:
                return p

n = int(pop_len())
nl = int(n/2)
hist_peo = []
people = []

#generates a list of people (chromossomes)
def population():
       #people = []
       for i in range(0,n):
           p = random.SystemRandom().uniform(0, math.pi)
           if p == math.pi:
               p = round(p)                             
           else:
               p
               print(p)
               person = get_bits(p)
               print(person)
               people.append(person)
       return  people


for i in range(n-nl):
        population() 
        a = list(x for x in population())
hist_peo.extend(a)
print(hist_peo)
print(len(hist_peo))

fitnessList = []
hist_fit = []

#fitness calculation for each chromossome
def calc_fitness():
        for t in range(len(people)):
                people[t] = get_float(people[t])
                fitness   = people[t] + abs(math.sin(32*people[t]))
                fitnessList.append(fitness) 

calc_fitness()
print(fitnessList)

weightsList = []

def calc_weights():
        for w in range(len(fitnessList)):
                weights = fitnessList[w]/ (sum(fitnessList)/len(fitnessList))
                weightsList.append(weights)

calc_weights()
print(weightsList)

couple = []

def roullette_selection(): 
        s = random.choices(people, weightsList, k = 2)
        for i in range(2):
                c = get_bits(s[i])
                couple.append(c)

roullette_selection()

print(couple) #couple selected

dad = couple[0] 
mom = couple[1]

descendants = []

#single point crossover 
def crossover():
        pc = random.randint(1,10)/10 
        if   0.1 <= pc <= 0.7:
                print('cruzamento resultou em: \n')
                d1 = dad[0:16]+mom[16:32]
                d2 = mom[0:16]+dad[16:32]
        else:
                print("copia identica \n")
                d1 = dad[:]
                d2 = mom[:]
        descendants.append(d1)
        descendants.append(d2)
        print("Descendants:" ,descendants)

crossover() 

new_population = []
chrome = []

#mutation
def mutation():
    #pm = random.randint(1,2)
    pm = 1
    if  pm == 1:
        sd = descendants[random.randint(0,1)]
        if sd == descendants[0]:
            new_population.append(descendants[1])
        else:
            new_population.append(descendants[0])
            ap = random.randint(0,32)
            if sd[ap] == '0':
                m = '1'
            else:
                m = '0'
                md = sd[:ap] + m + sd[ap+1:]
                new_population.append(md)
                print("selected descendant:",sd)
                print("position:",ap)
                print("the mutated chromossome is: \n",md)
    else:
        new_population.append(descendants[0])
        new_population.append(descendants[1])
        print("doesn't occurred a mutation")

mutation()
for i in new_population:
            chrome.append(i)
            print("New chromossomes: ", chrome)

print("done!")
print("population length: ", len(chrome))