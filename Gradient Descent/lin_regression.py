import numpy as np
import matplotlib.pyplot as plt

def f_true(x):
    return 2 + 0.8*x

#conjunto de treinamento {(x,y)} + ruido
xs = np.linspace(-3,3,100)
ys = np.array( [f_true(x) + np.random.randn()*0.5 for x in xs])

#hipotese
def h(x, theta):
    return theta[0] + theta[1]*x

#funcao de custo 
def J(theta, xs, ys):
    soma = 0
    for x, y in zip(xs, ys):
        soma += (h(x, theta) - y) ** 2
    return (1/(2*len(xs))) * soma


#derivada parcial com respeito a theta[i]
#if x_i = theta0 --> 1 senao theta1
def gradient(i, theta, xs, ys):
    soma = 0
    for x, y in zip(xs, ys):
        x_i = 1 if i == 0 else x
        soma += ( h(x, theta) - y) * x_i
    return (1.0/len(xs)) * soma

'''plota no mesmo grafico: - o modelo/hipotese (reta)
   - a reta original (true function)
   - e os dados com ruido (xs,ys)
'''
def print_modelo(theta, xs, ys):
    
    #modelo
    plt.figure()
    ys_ = np.array( [h(x, theta) for x in xs])
    plt.plot(xs, ys_, 'b', label = "Modelo" )
    
    #true
    ys_ = np.array( [f_true(x) for x in xs])
    plt.plot(xs ,ys_, 'r', label = "Funcao verdadeira")

    ##dataset
    plt.plot(xs, ys, 'og', label = "Dados")

    plt.xlim([-3,3])
    plt.legend()
    plt.show()


theta = np.zeros(2) #hipotese inicial
alpha  = 0.1       #taxa de aprendizagem -> 0.9 alta: diverge ; 0.1 boa: converge rapido ; 0.0001 converge lentamente

custo  = [ ]
tz     = [ ]
tum    = [ ]
epochs = 5000

for k in range(epochs):
    t0 = theta[0] - alpha * gradient(0, theta, xs, ys)
    t1 = theta[1] - alpha * gradient(1, theta, xs, ys)
    theta[0] = t0
    theta[1] = t1
    tz.append(theta[0])
    tum.append(theta[1])
    custo.append( J(theta, xs, ys))

print_modelo(theta, xs, ys)


#funcao custo ao longo das iteracoes
plt.figure()
x = [f for f in range(epochs)]
y = [e for e in custo]
plt.plot(x, y, 'm', label = "iters v Cost fcn" )
plt.legend()
plt.show()

#funcao de custo em funcao dos parametros theta[0] e theta[1]:
plt.figure()
x  = [f for f in tz]
y  = [e for e in custo]
plt.plot(x, y, 'b', label = "theta0 v  Cost fcn" )
plt.legend()
plt.show()

plt.figure()
x2 =  [g for g in tum]
y  =  [e for e in custo]
plt.plot(x2, y, 'g', label = "theta1 v Cost fcn" )
plt.legend()
plt.show()