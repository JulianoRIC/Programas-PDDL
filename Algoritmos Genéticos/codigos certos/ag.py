#Juliano Ricardo da Silva
#Não usei o template fornecido

#Algoritmo genético 

L = 4 * 8 #size of chromossome in bits

import struct
import random
import math
import matplotlib.pyplot as plot
import numpy as np
import os

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
        p = int(input("digit the size of population:  "))
        if (p<=2): 
                print("minimum value is 4")
                p = 4
                return p
        elif(p%2 != 0):
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
                #if fitness doesnt respect the limits [0,pi), their fitness is equal zero to avoid their spread
                if fitness < 0 or fitness > math.pi:
                        fitness = 0 
                        fitnessList.append(fitness)
                else:        
                     fitnessList.append(fitness)
        return fitnessList

#selects two chromossomes to posterior crossover
def roullette_selection(listpop,fit):
        store = [] 
        st = []
        while not(len(store) == 2):
                        store.extend((random.choices(listpop,fit,k=1)))
                        for i in store:  
                              st.append(get_bits(i))
        #while there are two chromossomes
        while st[-1] == st[-2]:
              print("********************TWO EQUAL CHROMOSSOMES, MAKE NEW SELECTION************")                                       
              st = []  
              store.extend((random.choices(listpop,fit,k=1))) #repeat selection in population
              for i in store: st.append(get_bits(i))
        return  st[-2:]

def roullette(lst, ft):
        store2 = []
        c = 0
        while not(len(store2) == 2):
                        lst=lst[-n:]
                        ft = ft[-n:]
                        store2.extend((random.choices(lst,ft,k=1))) 
        while (store2[-1] == store2[-2]): #and c != 50):
              print("********************TWO EQUALS CHROMOSSOMES, MAKE NEW SELECTION************")                                       
              store2[-1] = lst[0+c]
              store2[-2] = lst[-1+c]
              c+=1
              print("NOW, THE COUPLE IS: ", store2)
        return store2

#single point crossover 
def crossover():
        pc = random.randint(1,10)/10 
        if pc > 1: pc = 1
        if pc < 0.1: pc = 0.1
        if   0.1 <= pc <= 0.7:
                print('crossover resulted in: \n')
                d1 = dad[0:16]+mom[16:32]
                d2 = mom[0:16]+dad[16:32]
                print(d1,d2)
        else:
                print("identhical copy \n")
                d1 = dad[:]
                d2 = mom[:]
        descendants.append(d1)
        descendants.append(d2)
        return descendants

#mutation
def mutation():
    pm = random.randint(1,1000)
    if pm > 1000: pm = 1000 
    if pm < 1: pm = 1
    if  pm == 1:
        md = []
        sd = descendants[random.randint(0,1)]
        if sd == descendants[-2]:
            new_population.append(descendants[-1])
        else:
            new_population.append(descendants[-2])
            
        ap = random.randint(0,32) 
        if (0 >= ap or ap >= 32): ap = 0
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
def calc_avg_fitness(newfit):
                avg_fit = sum(newfit)/g 
                return avg_fit


chrome = []
n = pop_len()
g = n
iterations = 0
new_pop = []
iters = gen_len()
people = []
new_chrome = []
chromossome = []
avg = []
firstgen = []
secgen = []
lastgen = []

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
            avg.append(calc_avg_fitness(fitnessList)) #calculates the average fitness of the first population    
            print("\n******AVERAGE FITNESS: ",avg)     
            while(len(chrome) != g):    
                couple = []
                couple = roullette_selection(people,fitnessList) #selects a couple of chromossomes
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
            new_gen = chrome
            print("\n*****population list to create next generation is*****\n", new_gen)
            for i in new_gen:
                firstgen.append(get_float(i))
    
    #if the first generation was created, the new one will be generated based on the fitnesslist from previous generation
    if(people != []):
                for i in new_gen:
                         new_pop.append(i)
                         chromossome = []
                         x = []
                         new_population = []
                         fitnessList = []
                         descendants = []
                         new_chrome = []
     
    #is the first generation already created? therefore, repeats the natural selection process for each next generation
    if(iterations >= 2 and len(avg) != iters):
            print("**************************************************")
            print("*****************GENERATION NUMBER: ", iterations)
            print("**************************************************")
            print("\n New population is: \n",   new_pop[-n:])
            calc_fitness(new_pop[-n:])
            print("\n New fitness list is: \n", fitnessList[-n:])
            avg.append(calc_avg_fitness(fitnessList[-n:]))        
            #while number of chromossomes is different of population size, repeats the process
            while(len(chromossome) != g):    
                    x = []
                    x = roullette(new_pop, fitnessList)#selects two chromossomes to crossover
                    print("\n*****Couple selected:  *****\n", x[-n:])
                    dad = x[0] 
                    mom = x[1]
                    crossover()
                    mutation()
                    for i in [new_population[-2],new_population[-1]]:
                            new_chrome.append(i)
                    chromossome.extend([new_chrome[-2],new_chrome[-1]])    
                    print("\n*****New chromossomes******\n", chromossome)
                    

            new_gen  = chromossome
            print("\n*****population list to create next generation is*****\n", new_gen)


    if(iterations == 10):
        for j in chromossome:
                secgen.append(get_float(j))
    if(iterations == 600):
        for k in chromossome:
                lastgen.append(get_float(i))

                                      
print("done!")
print("population length: ", len(chrome))
print("AVG FITNESS LIST: ", avg)

print("FIRST GEN:", firstgen)
print("SECOND GEN:", secgen)
print("LAST GEN:", lastgen)

#avg.insert(0,0)

#plot avg fitness list
xx_value = list(range(0,iters)) 
yy_value = [f for f in avg]
plot.plot(xx_value, yy_value, label = "Average fitness list")
plot.legend()
plot.show()

yval  = [f for f in firstgen] #1st generation chromossomes
yval2 = [g for g in secgen]   #10th generation chromossomes

fg = []
sg = []
lg = []

#calculates the fitness from the generations of chromossomes selected
def fit_gen(g,h):
        for t in g:
                fitness   = t + abs(math.sin(32*t))
                h.append(fitness)
        return h


fit_gen(firstgen, fg)
fit_gen(secgen,   sg)
fit_gen(lastgen, lg)

print("FIRST FIT GEN:", fg)
print("SECOND FIT GEN:", sg)
print("LAST FIT GEN:", lg)


#math fitness function 
x = np.linspace(0,math.pi,200)
y =  x + abs(np.sin(32*x))

#plot fitness function vs x and chromossomes vs fitness
fig, ax = plot.subplots()
ax.plot(x, y, color ='blue', label = "fitness function")
ax.scatter(firstgen, fg, color='orange', label = "Chomossomes First Gen")
ax.scatter(secgen, sg, color='black', label =    "Chomossomes Sec Gen")
ax.scatter(lastgen, lg, color='green', label =   "Chomossomes Third Gen")

plot.legend()
plot.show()

#pause 
os.system("pause")
