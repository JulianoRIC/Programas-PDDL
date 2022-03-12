#Backpropagation Algorithm

import math
import random 
import numpy as np

#lista de pesos
weights = []

#metodo de Xavier para inicializacao randomica dos pesos
'''
def weights_ini(n,m):
    for i in range(m*n):
       weights.append(random.uniform(-(1/math.sqrt(n)), 1/math.sqrt(n)))
    print("Pesos: ", weights)
    return weights
'''

#n = numero de neuronios (ou entradas) na camada L
#m = numero de neuronios na camada L+1

#weights = weights_ini(3,2)

#definindo o conjunto de treinamento (x,y) = (entradas, saídas desejadas)
x = [0.05, 0.1]   
y = [0.01, 0.99]

#inicializando a rede neural 
def create_network(i, h, o):
    hidden  = []
    outputs = []
    for j in range(h): hidden.append(1)
    for k in range(o): outputs.append(1)
    return i, hidden, outputs

net = create_network(x,2,2)
print(net)



u    = []
g_uo = []
bias = [0.35, 0.6]
weights = [0.15, 0.2, 0.25, 0.3, 0.4, 0.45, 0.5, 0.55]


def propagation(ins, l, b):
    for j in range(len(net[l])):
        u.append(np.dot(ins, weights[j*2:2*(j+1)]) + bias[b]*1)
    return u

print(propagation(x, 1, 0))

def activation(neuron):
    for j in range(len(neuron)): 
        g_uo.append(1/(1+math.exp(-neuron[j])))
    return g_uo

