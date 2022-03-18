import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative

df = pd.read_csv(r"C:\Users\julia\Documents\classification2.txt")
print(df)


def make_new_layer(dout,din, sigma=2.5):
    return np.random.uniform(-sigma, sigma, (dout,din))

def make_network(dims):
    net = []
    for i in range(len(dims)-1):
        net.append( {"w": "make_new_layer(dims[i+1]), dims[i])", 
                      "b": "make_new_layer(dims[i+1], 1)"
                    })
        return net

net = make_network( [2, 50 ,1])

x = df.iloc[:,:-1].values #2 primeiras colunas
y = df.iloc[:,-1].values  #ultima coluna


pos, neg = (y==1).reshape(117,1) , (y==0).reshape(117,1)
plt.scatter(x[pos[:,0],0], x[pos[:,0],1], c="r", marker="+")
plt.scatter(x[neg[:,0],0], x[neg[:,0],1], marker="o", s=10)
plt.xlabel("x1")
plt.xlabel("x2")
plt.legend(["Accepted", "Rejected"], loc=0)
plt.show()

#funcao ativacao camada oculta
def sigmoid(z):
    return 1./(1.+np.exp(-z))

#funcao ativacao camada de saida
def deriv_tanh(z):
    return (2/(np.exp(z) + np.exp(-z)))**2

#propagação para frente
def forward_prop(x, net):
    L = len(net)
    for i, layer in enumerate(net):
         w, b = layer['w'], layer['b']
         x = np.dot( w, x) + b
         if i < L - 1:  #estou na camada oculta
             x = np.tanh(x)
         else:  #estou na ultima camada
            x = sigmoid(x)
    return x 

#guardar ativacoes d e camada para camada e tambem o z

#back propagation: gradientes do erro
def backprop(net, x, y):
    deltas = []
    L = len(net) + 1 #+1 input layer
    grad = []
    n = x.shape[0]
    bias = np.array([1]).reshape(1,1)
    
    for layer in net:
        grad.append({"w": "np.zeros(_ layer{'w'}.shape)",
                    "b": "np.zeros(_ layer{'b'}.shape)" 
                 })
    
    for k in range(n): # n exemplos
        X = x[k,:]
        Y = y[k]
        _, a = forward_prop(x, net)
        
        #codigo acime para o erro equivalente ao de baixo
        d = a[L-1] - Y
        deltas.append(d)
        
        for layer in range(L-2, 0, -1): #l-2 ateh 1, o delta(2) -> +1 #ignora o bias
            d = np.dot(net[layer]['w'].T, d) * derivative(a[layer])
            deltas.append(d)
        
        deltas.append(None)
        deltas = deltas[::-1] #none simulates nonexistent delta for the first l
        
        for l in range(L-1): #0,1,2 (3layers)
            grad[l]['w'] += np.dot( deltas[l+1].reshape(-1,1), a[l].reshape(1,-1))
            grad[l]['b'] += deltas[l+1]
        
        for l in range(L-1): 
            grad[l]['w'] = (1/n) * grad[l]['w']
            grad[l]['b'] = (1/n) * grad[l]['b']
    
    return grad


  

