
class Neural_Network:
      
    feature = None #number of inputs/features
    hidden  = None #number of neurons of hidden layer
    label   = None #number of outputs 

    def __init__(self, feature, hidden, label):
        self.feature = feature
        self.hidden  = hidden
        self.label   = label
        

