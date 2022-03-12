
class Pessoa:
    nome = None
    idade = None

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def getAno(self, anoAtual):
        return anoAtual - self.idade

pessoa = Pessoa("Jul", 22)
print(pessoa.getAno(2010))

class Neural_net:
    
    features = None
    hidden = None
    outputs = None

    def __init__(self, features, hidden, outputs):
        self.features = features
        self.hidden = hidden
        self.outputs = outputs
    
    def create_network(self, feature, hidden, outputs):
        features= feature
        hidden  = []
        outputs = []
        for j in range(self.hidden): hidden.append(1)
        for k in range(self.outputs): outputs.append(1)
        return features, hidden, outputs

net = Neural_net(2,2,2).create_network(2,2,2)
