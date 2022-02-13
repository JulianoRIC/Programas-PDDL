#Algoritmo genético 


L = 4 * 8 #size of chromossome in bits

from ast import Store
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
global n 

#gets population size by user input
def pop_len():
        p = int(input("digit the number of population:  "))
        if(p%2 != 0):
                print("odd number")
                p = p - 1
                print("changed to even")
                return p
        else:
                return p

#gets the generation number by user input  
def gen_len():
        p = int(input("digit the number of generations:  "))
        return p

#generates a random list of people (chromossomes)
def population():
        for i in range(g):
                p = random.SystemRandom().uniform(0, math.pi)
                person = get_bits(p)
                people.append(person)
                
#fitness calculation for each chromossome
def calc_fitness(p):
        for t in range(len(p)):
                p[t] = get_float(p[t])
                fitness   = p[t] + abs(math.sin(32*p[t]))
                fitnessList.append(fitness)
        return fitnessList

#selects two chromossomes to posterior crossover
def roullette_selection(listpop):
        store = [] 
        while not(len(store) == 2):
                if(iterations == 1): store.append(get_bits(random.choice(listpop)))
        return store

#single point crossover 
def crossover():
        pc = random.randint(1,10)/10 
        if   0.1 <= pc <= 0.7:
                print('crossover resulted in: \n')
                d1 = dad[0:16]+mom[16:32]
                d2 = mom[0:16]+dad[16:32]
        else:
                print("identhical copy \n")
                d1 = dad[:]
                d2 = mom[:]
        descendants.append(d1)
        descendants.append(d2)
        print(descendants)
        return descendants

#mutation
def mutation():
    pm = random.randint(1,50)
    if  pm == 1:
        md = []
        sd = descendants[random.randint(0,1)]
        if sd == descendants[-2]:
            new_population.append(descendants[-1])
        else:
            new_population.append(descendants[-2])
            
        ap = random.randint(0,32) 
        if (0 > ap or ap > 32): ap = 0
        if sd[ap] == '0':
                m = '1' 
        else:
                m = '0'
        md = sd[:ap] + m + sd[ap+1:]
        print("selected descendant:",sd)
        print("position:",ap)
        print("the mutated chromossome is: \n",md)
        new_population.append(md)
        return new_population
    else:
        new_population.append(descendants[-2])
        new_population.append(descendants[-1])
        print("doesn't occurred a mutation")
    return new_population

#fitness calculation for each chromossome after their evolution
def calc_new_fitness():
        for t in range(len(x)):
                fitness = x[t] + abs(math.sin(32*x[t]))
                new_fitnessList.append(fitness)
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


while iterations != iters:
    iterations+=1

    #first generation to be created and selected until chromossomes_evolved = size of population
    if(iterations==1 and people ==[]):
            print("*****************GERACAO NRO **************", iterations)
            print("The population number is ", g)
            population()   #population
            print("\n*****The population of chromossomes in bit chain: ***** \n",people)
            fitnessList = []
            calc_fitness(people) #calculates the fitness for each chromossome
            print("\n*****List of fitness: *****\n ",fitnessList)
            while(len(chrome) != g):    
                couple = []
                couple = roullette_selection(people) #selects a couple of chromossomes
                print("\n*****The selected couple is: *****\n", couple)
                dad = couple[0] 
                mom = couple[1]
                descendants = []
                crossover() #chromossomes crossover (or not) to generate descendants
                new_population = []
                mutation()  #chromossomes mutation (or not) to generate descendants               
                for i in new_population:
                    chrome.append(i)
                    print("\n*****New chromossomes: ******\n",chrome) #the new population of chromossomes
            x = []
            new_fitnessList = []
            for j in chrome:
               x.append(get_float(j))
               #print("In numbers:", x)  #just for debbug
            calc_new_fitness()           #calculates the new fitness of the evolved population
            print("\n*****List of fitness after evolution: *****\n", new_fitnessList)
 
    
    #if the first generation was created, the new one will be generated based on the fitnesslist from previous generation
    if(people != []):
                for i in new_fitnessList:
                         person = get_bits(i)
                         new_pop.append(person)
                         chromossome = []
                         x = []
                         new_population = []
                         fitnessList = []
                         descendants = []
                         new_chrome = []
     
    #is the first generation already created? so repeats the natural selection process for each next generation
    if(iterations >= 2):
            print("**************************************************")
            print("*****************GENERATION NUMBER: ", iterations)
            print("**************************************************")
            print("\nNew population is: \n", new_pop[-n:])
            calc_fitness(new_pop[-n:])
            print("\nNew fitness list is: \n", fitnessList[-n:])
            #while number of chromossomes is different of population size repeats the process
            while(len(chromossome) != g):    
                    x = []
                    #selects two chromossomess to crossover (or not)
                    while not(len(x) == 2):
                           s=random.choice(new_pop[-n:])
                           a = s
                           x.append(a)
                    print("\n*****Couple selected:  *****\n", x[-n:])
                    dad = x[0] 
                    mom = x[1]
                    crossover()
                    #print("\n*****Crossover: *****\n", [descendants[-2], descendants[-1]])
                    mutation()
                    #print("\n*****Mutation: ******\n", [new_population[-2], new_population[-1]])
                    for i in [new_population[-2],new_population[-1]]:
                            new_chrome.append(i)
                    chromossome.extend([new_chrome[-2],new_chrome[-1]])    
                    print("\n*****New chromossomes******\n", chromossome)

            fitnessList = []    
            calc_fitness(chromossome)  #calculates the fitness list to create the next generation
            new_fitnessList = fitnessList.copy()
            print("\n*****fitness list to create next generation is*****\n", new_fitnessList)
                                      
print("done!")
print("population length: ", len(chrome))
