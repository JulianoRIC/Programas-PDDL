#Backpropagation Algorithm

import math
import random
from re import M 
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


#camada de entrada, camada oculta (dois neuronios), camada de saida (dois neuronios)
net = create_network(x,2,2)
print(net)

u    = []
g_uo = []
bias = [0.35, 0.6]
weights = [0.15, 0.2, 0.25, 0.3, 0.4, 0.45, 0.5, 0.55]

#propagacao entrada para camada oculta
for j in range(len(net[1])):
        u.append(np.dot(x, weights[j*2:2*(j+1)]) + bias[0]*1)
print("Propagação para camada oculta: ", u)

#funcao generica de ativacao dos neuronios
def activation(neuron):
    for j in range(len(neuron)): 
            g_uo.append(1/(1+math.exp(-neuron[j])))
    return g_uo

g = g_uo
#mostra ativacao dos neuronios da camada oculta
print("Ativacao neuronios da camada oculta: ", activation(u))

u2 = []

#propagacao camada oculta para camada de saída
for j in range(len(net[2])):
    u2.append(np.dot(g_uo, weights[4+j*2:2*(j+1)+4]) + bias[1]*1)

print("Propagacao para camada de saída: ", u2)


#ativacao dos neuronios da camada de saída
g_uo = []
print("Ativacao neuronios da camada de saída: ", activation(u2))
g.extend(g_uo)

print("G historico", g)

erros = [ ]

#calculando erro total
def erroTotal():
    for i in range(len(y)):
        erros.append(0.5*(y[i] - g_uo[i])**2)
    Etot = sum(erros)
    return Etot

print("Erro total eh: ", erroTotal())

#Corrigindo os pesos da camada oculta para camada de saída

#derivada do Etotal em relacao a g_uo
def derivada_guo(y, g):
    return -(y - g)

#derivada do g_uo em relacao a uo
def derivada_uo(g):
    return g*(1-g)

#derivada de uo em relacao ao peso w
def derivada_w(gu):
    return gu

#derivada total do erro em relacao ao peso w da camada oculta
def derivada_etot(dg, du, dw):
    return dg*du*dw

#taxa de aprendizagem
a = 0.5

#calculando gradiente do w da camada oculta
def gradient_hidden(w, a, dtot):
    return w - a*dtot

'''
#calculando w5
# print("Derivada guo", derivada_guo(y[0], g_uo[0]))
print("Derivada uo", derivada_uo(g_uo[0]))
print("Derivada g", derivada_w(g[0]))
dtot =derivada_etot(derivada_guo(y[0], g_uo[0]),derivada_uo(g_uo[0]),derivada_w(g[0]))
print("Derivada total", dtot)
print("Gradiente eh", gradient_hidden(weights[4], a, dtot))
'''

dg = derivada_guo(y[1], g_uo[1])
du = derivada_uo(g_uo[1])
dw = derivada_w(g[1])

dtot = derivada_etot(dg, du, dw)

grad = gradient_hidden(weights[7], a, dtot)

print("dtot: ", dtot)
print("gradiente:", grad)