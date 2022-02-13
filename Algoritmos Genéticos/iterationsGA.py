#Algoritmo genético 
#FEITO ATE CROSSOVERRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR

L = 4 * 8 #size of chromossome in bits

import struct
import random
import math
import string

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


def gen_len():
        p = int(input("digit the number of generations:  "))
        return p

#generates a list of people (chromossomes)
def population():
        for i in range(g):
                p = random.SystemRandom().uniform(0, 0.005) #era pi
                person = get_bits(p)
                print(person)
                people.append(person)
                
#fitness calculation for each chromossome
def calc_fitness(p):
        for t in range(len(p)):
                p[t] = get_float(p[t])
                fitness   = p[t] + abs(math.sin(32*p[t]))
                fitnessList.append(fitness)
        return fitnessList

def calc_weights(fL):
        for w in range(len(fL)):
                weights = fL[w]/(sum(fL))
                weightsList.append(weights)
        return weightsList

def roullette_selection(sel, wl): 
        s = random.choices(sel, wl, k = 2)
        for i in range(2):
                c = get_bits(s[i])
                couple.append(c)
        return couple

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
        #print(descendants[-n:])
        return descendants

#mutation
def mutation():
    pm = random.randint(1,6)
    if  pm == 1:
        sd = descendants[random.randint(0,1)]
        if sd == descendants[-2]:
            new_population.append(descendants[-1])
        else:
            new_population.append(descendants[-2])
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
        new_population.append(descendants[-2])
        new_population.append(descendants[-1])
        print("doesn't occurred a mutation")
    return new_population

#fitness calculation for each chromossome
def calc_new_fitness():
        for t in range(len(x)):
                fitness = x[t] + abs(math.sin(32*x[t]))
                new_fitnessList.append(fitness)
                #print("List of fitness: ", new_fitnessList)
        return new_fitnessList


chrome = []
n = pop_len()
g = n
iterations = 0
new_pop = []
iters = gen_len()
people = []
new_chrome = []
chromossome = []
next_gen = []


while iterations != iters:
    iterations+=1
    if(iterations==1 and people ==[]):
            print("*****************GERACAO NRO **************", iterations)
            print("population number is ", g)
            #people = []
            population()   #population
            print("Population of chromossomes:",people)
            fitnessList = []
            calc_fitness(people) #calculates the fitness for each chromossome
            print("List of fitness: ",fitnessList)
            weightsList = []
            calc_weights(fitnessList) #calculates the probab weights for each chromossome
            print("Prob weights:",weightsList)
            while(len(chrome) != g):    
                couple = []
                roullette_selection(people, weightsList) #selects a couple of chromossomes
                print("The couple selected: ", couple)
                dad = couple[0] 
                mom = couple[1]
                descendants = []
                crossover() #chromossomes crossover to generate descendants
                new_population = []
                #chrome = []
                mutation()                
                for i in new_population:
                    chrome.append(i)
                    print("New chromossomes: ",chrome)    
            x = []
            new_fitnessList = []
            for j in chrome:
               x.append(get_float(j))
               print("In n umbers:", x)
            calc_new_fitness()
            print("List fitness after evolution: ", new_fitnessList)
 
    if(people != []):
                print("PASSEI POR AQUIIIIIIIIIIIIIIIIIIIIIIIIIIII")
                for i in new_fitnessList:
                         person = get_bits(i)
                         new_pop.append(person)
                         chromossome = []
                         weightsList = []
                         x = []
                         next_gen = []
                         new_population = []
                         fitnessList = []
                         descendants = []
                         new_chrome = []
     
    if(iterations >= 2):
            
            print("*****************GERACAO NRO **************", iterations)
            print("JAJAAJAJAJAAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAAJAJJ")
            print("new population is: ", new_pop[-n:])
            calc_fitness(new_pop[-n:])
            print("Nova calc fitness: ", fitnessList[-n:])
            calc_weights(fitnessList[-n:])
            print("nova calc weights: ", weightsList[-n:])

            while(len(chromossome) != g):    
                    x = []
                    while not(len(x) == 2):
                           s=random.choice(new_pop[-n:])
                           a = s
                           x.append(a)
                    print("Nova couple selected:  ", x[-n:])
                    dad = x[0] 
                    mom = x[1]
                    crossover()
                    #print("DESCENDANTS:  ", descendants)    
                    print("Nova crossover: ", [descendants[-2], descendants[-1]])
                    #descendants = []    
                    mutation()
                    #print("NEW POPULATION: ", new_population)
                    print("Mutation: ", [new_population[-2], new_population[-1]])
                    for i in [new_population[-2],new_population[-1]]:
                            new_chrome.append(i)
                    chromossome.extend([new_chrome[-2],new_chrome[-1]])    
                    print("NOVA New chromossomes", chromossome)

            fitnessList = []    
            calc_fitness(chromossome)
            print("New Fitness list:", fitnessList)     
            new_fitnessList = fitnessList.copy()
            print("NOVA New fitness", new_fitnessList)
                    
                    
   #break

print("done!")
print("population length: ", len(chrome))






