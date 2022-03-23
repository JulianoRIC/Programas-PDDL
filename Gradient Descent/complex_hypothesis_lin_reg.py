from pyexpat import model
import numpy as np
import matplotlib.pyplot as plt

def f_true(x):
    return -0.3 + 0.2*x

#conjunto de treinamento {(x,y)} + ruido
xs = np.linspace(-3,3,15)
ys = np.array( [f_true(x) + np.random.randn()*0.6 for x in xs])


def features_complex(x):
    return np.concatenate((np.ones(1), [x, x**2, x**3]), axis=0)

def features_good(x):
    return np.concatenate((np.ones(1), [x]), axis=0)

#hipotese
def h_complex(x, theta):
    return np.dot(theta.T, features_complex(x))
def h_good(x, theta):
    return np.dot(theta.T, features_good(x))

#funcao de custo 
def J(theta, xs, ys, h):
    soma = 0
    for x, y in zip(xs, ys):
        soma += (h(x) - y) ** 2
    return (1/(2*len(xs))) * soma


#derivada parcial com respeito a theta[i]
#if x_i = theta0 --> 1 senao theta1
def gradient(i, theta, xs, ys, h, features):
    soma = 0
    for x, y in zip(xs, ys):
        soma += ( h(x) - y) * features(x)[i]
    return (1.0/len(xs)) * soma


'''plota no mesmo grafico: - o modelo/hipotese (reta)
   - a reta original (true function)
   - e os dados com ruido (xs,ys)'''

def print_modelo(theta, xs, ys, h):
    
    #modelo
    plt.figure()
    ys_ = np.array( [h(x) for x in xs])
    plt.plot(xs, ys_, 'b', label = "Modelo" )
    
    #true
    ys_ = np.array( [f_true(x) for x in xs])
    plt.plot(xs ,ys_, 'r', label = "Funcao verdadeira")

    ##dataset
    plt.plot(xs, ys, 'og', label = "Dados")

    plt.xlim([-3,3])
    plt.legend()
    plt.show()

def plot_allmodels(models):
    n = len(models)
    k = 1
    for chave_model in models():
        plt.title(chave)
        k+=1
        theta, h, _ = models[chave]
        hypothesis = lambda x: h(x,theta)
        print_modelo(theta, xs, ys, hypothesis)
    plt.show()


theta0 = np.zeros(shape=features_good(0).shape)
theta1 = np.zeros(shape=features_complex(0).shape)

models = {
    'good': [theta0, h_good, features_good],
    'complex': [theta1, h_complex, features_complex]
}

alpha  = 0.01       #taxa de aprendizagem -> 0.9 alta: diverge ; 0.1 boa: converge rapido ; 0.0001 converge lentamente

custo  = {
           'good': [],
           'complex': []
}

epochs = 3000

print('running...')


for chave, model in model.items:
    theta, h, features = model
    hypothesis = lambda x: h(x, theta)
    new_theta = [theta[i] - alpha*gradient(i, theta, xs, ys, hypothesis)]
    models[chave][0] = np.array(new_theta)

    custo[chave].append( J(theta, xs, ys, hypothesis))
    
    if k == 200000:
        plot_all_models(models)


plot(cust['good'], '.-', label = 'good')
plot(custo['complex'], '.-', label = 'complex')
plt.legend()
show()


plot_all_models(models)