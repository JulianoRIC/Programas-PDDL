# JULIANO RICARDO DA SILVA
#INTELIGENCIA ARTIFICIAL

#Algoritmo genético 

L = 4 * 8 #size of chromossome in bits

import struct
import random
import math
from statistics import mean
from statistics import median
import matplotlib.pyplot as plot
import numpy as np

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
global n 

def pop_len():
        p = int(input("digit the number of population:  "))
        if(p%2 != 0):
                print("odd number")
                p = p - 1
                print("changed to even")
                return p
        else:
                return p
                
#generates a list of people (chromossomes)
def population():
        for i in range(g):
                p = random.SystemRandom().uniform(0, math.pi)
                if p == math.pi:
                        p = round(p)                             
                else:
                        print(p)
                person = get_bits(p)
                print(person)
                people.append(person)
                
#fitness calculation for each chromossome
def calc_fitness():
        for t in range(len(people)):
                people[t] = get_float(people[t])
                fitness   = people[t] + abs(math.sin(32*people[t]))
                fitnessList.append(fitness)

#probab weights for selection
def calc_weights():
        for w in range(len(fitnessList)):
                weights = fitnessList[w]/ (sum(fitnessList))
                weightsList.append(weights)

#couple's selection 
def roullette_selection(): 
        s = random.choices(people, weightsList, k = 2)
        for i in range(2):
                c = get_bits(s[i])
                couple.append(c)

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
        print(descendants)

#mutation
def mutation():
    pm = random.randint(1,1000) 
    if  pm == 10:
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

#fitness calculation for each chromossome
def calc_new_fitness():
        for t in range(len(chrome)):
                chrome[t] = get_float(chrome[t])
                fitness   = chrome[t] + abs(math.sin(32*chrome[t]))
                new_fitnessList.append(fitness)
                print("List of fitness: ", new_fitnessList)
        return new_fitnessList

chrome = []
n = pop_len()
g = n
hist = []
new_fitnessList = []
avg_fit = []
novalista =  []
alist = []
nl = int(2*g)
new_people = []
flag = 0
people = []

while True:
    while(not(len(chrome) == nl)):    
        print("**********************************************************************************************")
        print("*******************************NEW ITERATION**************************************************")
        print("**********************************************************************************************")
        #people = []
        if people == []:
                population()   #population
                print("Population of chromossomes:",people)
        else:
                people = new_people
                print("Poulation of chromossomes JALDALHSADL: ", people)
        fitnessList = []
        calc_fitness() #calculates the fitness for each chromossome
        print("List of fitness: ", fitnessList)
        weightsList = []
        calc_weights() #calculates the probab weights for each chromossome
        print("Prob weights:",weightsList)
        couple = []
        roullette_selection() #selects a couple of chromossomes
        print("The couple selected: ", couple)
        dad = couple[0] 
        mom = couple[1]
        descendants = []
        crossover() #chromossomes crossover to generate descendants
        new_population = []
        mutation()                
        for i in new_population:
            chrome.append(i)
        print("New pop is:  ", chrome) #[-g:]
        #people = chrome 
        #print("Proxima pop = nova pop", people)    
        calc_new_fitness()
        for i in new_fitnessList:
                person = get_bits(i)
                new_people.append(person)
                print("NOva populacao e ", new_people)
    #h = int(2)
    #alist = list(np.average(np.reshape(new_fitnessList, (-1, h)), axis=1))
    #print("Average fitness list: ", alist)
    
    break

print("done!")
print("population length: ", len(chrome))



'''
x_values = list(range(0,g,2))
y_values = [f for f in alist]
plot.plot(x_values, y_values)
plot.show()


xx_value = list(range(0,len(new_fitnessList))) 
yy_value = [f for f in fitnessList]
y2_value = [g for g in new_fitnessList]

plot.plot(xx_value, yy_value, label = "fitnessList")
plot.plot(xx_value, y2_value, label = "newfitnessLis")
plot.legend()
plot.show()
'''