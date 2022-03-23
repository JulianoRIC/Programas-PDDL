from cmath import log
import numpy as np
from matplotlib.pyplot import subplot, plot, show, clf, vlines
import matplotlib.pyplot as plt

#conjunto de treinamento {(x,y)}
mean0 , std0 = -0.4 , 0.5
mean1 , std1 =  0.9 , 0.3 
m = 200

x1s = np.random.randn(m//2) * std1 + mean1
x0s = np.random.randn(m//2) * std0 + mean0
xs  = np.hstack((x1s , x0s))

ys  = np.hstack(( np.ones(m//2), np.zeros(m//2)))

plot(xs[:m//2], ys[:m//2], '.')
plot(xs[m//2:], ys[m//2:], '.')

plt.show()


def sigmoid(z):
    return 1/(1 + np.exp(-z))

'''hipotese sigmoid(theta[0] + theta[1] * x'''

def h(x,theta):
    return sigmoid(theta[0] + theta[1]*x)

'''funcao de custo para um exemplo; entropia cruzada'''
def cost(h, y):
    return -log(h) * y -log(1-h)*(1-y)

'''funcao de custo total'''
def J(theta, xs, ys):
    soma = 0
    for x, y in zip(xs, ys):
        soma += cost(h(x, theta), y)
    return (1/(len(xs))) * soma

'''derivada parcial em relacao a theta[i]'''
def gradient(i, theta, xs, ys):
    soma = 0
    for x, y in zip(xs, ys):
        x_i = 1 if i == 0 else x
        soma += ( h(x, theta) - y) * x_i
    return (1.0/len(xs)) * soma


def classifica(h):
    return h >= 0.5

'''Fronteira de decisao
h(x) = g(t0 + t1*x) = 0.5 <-> t0 + t1*x = 0 -> x = -t0/t1 
'''
def fronteira(theta):
    return -theta[0]/theta[1]

def plot_fronteira(theta):
    vlines(fronteira(theta), 0 , 1)

def accuracy(ys, predictions):
    num = sum(ys == predictions)
    return num/len(ys)

'''plota em subplots: os dados com a fronteira de decisao
e os dados classificados'''
def print_modelo(theta, xs, ys):
   
    #modelo
    plt.figure()
    ys_ = np.array( [h(x, theta) for x in xs])
    plt.plot(xs, ys_, 'b', label = "Modelo" )
    
    ##dataset
    plt.plot(xs, ys, 'og', label = "Dados")

    plt.xlim([-3,3])
    plt.legend()
    plt.show()

alpha  =  0.1
epochs = 2000
theta  = np.zeros(2)
custo = []
predictions =  []

print_modelo(theta, xs , ys)


for k in range(epochs):
    t0 = theta[0] - alpha * gradient(0, theta, xs, ys)
    t1 = theta[1] - alpha * gradient(1, theta, xs, ys)
    theta[0] = t0
    theta[1] = t1
    custo.append( J(theta, xs, ys))

#funcao custo ao longo das iteracoes
plt.figure()
x = [f for f in range(epochs)]
y = [e for e in custo]
plt.plot(x, y, 'og', label = "iters v Cost fcn" )
plt.legend()
plt.show()

#acuracia ao longo das iters
#plt.figure()
#x = [f for f in range(epochs)]
#y = [e for e in erro]
#plt.plot(x, y, 'm', label = "Accuracy" )
#plt.legend()
#plt.show()
