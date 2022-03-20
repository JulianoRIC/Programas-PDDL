#Autores: Juliano Ricardo e Guilherme Ludwig


#bibliotecas
import math
import random
from re import M
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


########################################################################################################################

#Extração de todos os exemplos (entradas) do conjunto de treinamento
df = pd.read_csv(r"C:\Users\julia\Documents\classification2.txt")
print(df)

x = df.iloc[:,:-1].values #2 primeiras colunas
y = df.iloc[:,-1].values  #ultima coluna

#plote dos exemplos a serem separados
pos, neg = (y==1).reshape(117,1) , (y==0).reshape(117,1)
plt.scatter(x[pos[:,0],0], x[pos[:,0],1], c="r", marker="+")
plt.scatter(x[neg[:,0],0], x[neg[:,0],1], marker="o", s=10)
plt.xlabel("x1")
plt.ylabel("x2")
plt.legend(["Accepted", "Rejected"], loc=0)
plt.show()
##################################################################################################################################


#Multi layer Perceptron - Rede Neural  


#inicializando a rede neural 
def create_network(i, h, o):
    hidden  = []
    outputs = []
    for j in range(h): hidden.append(1)
    for k in range(o): outputs.append(1)
    return i, hidden, outputs

#camada de entrada, camada oculta (dois neuronios), camada de saida (dois neuronios)
net = create_network(x,2,1)
print(net)

#lista de pesos
weights = []

#metodo de Xavier para inicializacao randomica dos pesos
def weights_ini(n,m):
    #n = nro de entradas e m= nro de neuronios da camada oculta
    for i in range(n*m+m):
       weights.append(random.uniform(-(1/math.sqrt(n)), 1/math.sqrt(n)))
    print("Pesos: ", weights)
    return weights

#cria aleatoriamente os pesos de acordo com o numero de entradas e numero de neuronios da camada oculta
weights = weights_ini(2, len(net[1]))

bias = []
#n eh o numero de layers da rede
def bias_ini(n):
    for i in range(n):
        bias.append(np.random.uniform(0, 1))
    return bias

print("Lista de bias: ", bias_ini(2))


#definindo o conjunto de treinamento (x,y) = (entradas, saídas desejadas)
x = [0.1, 0.2]   
y = [1]


u    = []
gu   = []
bias = [0.5, 0.1]

#propagacao entrada para camada 
for j in range(len(net[1])):
        u.append(np.dot(x, weights[j*2:2*(j+1)]) + bias[0]*1)
print("Propagação para camada oculta: ", u)


#funcao generica de ativacao dos neuronios
def activation(neuron):
    for j in range(len(neuron)): 
            gu.append(1/(1+math.exp(-neuron[j])))
    return gu

g = gu
#mostra ativacao dos neuronios da camada oculta
print("Ativacao neuronios da camada oculta: ", activation(u))

o = []

#propagacao camada oculta para camada de saída
for j in range(len(net[2])):
    o.append(np.dot(gu, weights[len(net[1])*len(x)+j*2:2*(j+1)+len(net[1])*len(x)]) + bias[1]*1)

print("Propagacao para camada de saída: ", o)

#funcao ativacao camada de saida
def act_tanh(z, i):
    for i in range(len(z)):
            gu.append((2/(1+np.exp(-2*z[i])))-1)
    return gu

#ativacao dos neuronios da camada de saída
gu = []
go = act_tanh(o,0)
print("Ativacao neuronios da camada de saída: ", go)

g.extend(go)
print("historico ativacoes", g)


#calculando erro total
erro = 0.5*(y[0] - go[0])**2

print("Erro total eh: ", erro)


#Corrigindo os pesos da camada oculta para camada de saída

#derivada do Etotal em relacao a go
def derivada_go(y, go, i):
    return -(y[i] - go[i])

dgo = derivada_go(y, go, 0)
print("Derivada erro em relacao a go1: ", dgo)

#derivada do go em relacao a o
def derivada_o(go, i):
    return (2/(np.exp(go[i]) + np.exp(-go[i])))**2


do = derivada_o(go, 0)
print("Derivada de go em relacao a o: ", do)

delta1 = dgo*do
print("Delta 1 eh: ", delta1)

#seleciono somente as ativacoes da camada oculta
gu = g[0:len(net[1])]

dw = [ ] 

#derivada de o em relacao ao peso w
def derivada_w(gu):
    for i in range(len(gu)):
        dw.append(gu[i])
    return dw

dw = derivada_w(gu)
print("As derivadas em relacao aos pesos da camada oculta  sao: ", dw)


dtot = np.dot(delta1, dw)

print("As derivadas do erro em relacao aos pesos da camada oculta sao:", dtot)

gh = []  #vetor para guardar os gradientes da camada oculta
a = 0.5 #taxa de aprendizagem

#calculando gradiente do w da camada oculta
def gradient_hidden(w, a, dtot):
    for i in range(len(net[1])):
        gh.append(w[i+4] - a*dtot[i])
    return gh

grad = gradient_hidden(weights, a, dtot)
print("Novos pesos da camada oculta em funcao do gradiente do erro sao: ", grad)

#vetor dos pesos atualizados
w_updated = [0, 0, 0, 0, 0, 0]
w_updated[4] = grad[0] 
w_updated[5] = grad[1] 

print("Pesos atualizados: ", w_updated)

#corrigindo os pesos camada1->camada oculta

#derivada do erro em relacao a O1
de_o1 = dgo*do
#print("Deo1", de_o1)
do_gu = weights[4]
#print("Do gu", do_gu)

#derivada do gu em relacao a u
def derivada_gu(guu, i):
    return guu[i]*(1-guu[i])

dg_u  = derivada_gu(g, 0)
#print("Dgu ", dg_u)

h1 = de_o1*do_gu*dg_u
print("O valor de h1 eh", h1)

dw = []
dw_first = derivada_w(x)

dtot_w1 = np.dot(h1, dw_first)

print("Derivadas parciais do erro em relacao a w1 e w2: ", dtot_w1)

do_g   = weights[5]
dg_u2  = derivada_gu(g, 1)

h2 = de_o1*do_g*dg_u2 
print("O valor de h2 eh: ", h2)

dtot_w2 = np.dot(h2, dw_first)

print("Derivadas parciais do erro em relacao a w3 e w4: ", dtot_w2)


ghs = []

#calculando gradiente do w da camada de entrda
def gradient_in(w, a, dtot,j):
    for i in range(len(net[1])):
        ghs.append(w[i+j] - a*dtot[i])
    return ghs

grad_2 = gradient_in(weights, a, dtot_w2,0)
print("Novos pesos w1 e w2 da camada oculta em funcao do gradiente do erro sao: ",  grad_2)

w_updated[0] = grad_2[0] 
w_updated[1] = grad_2[1]


ghs = []
grad_3 = gradient_in(weights, a, dtot_w2,2)
print("Novos pesos w3 e w4 da camada oculta em funcao do gradiente do erro sao: ",  grad_3)


w_updated[2] = grad_3[0] 
w_updated[3] = grad_3[1]

print("Todos os pesos corrigidos: ", w_updated)




