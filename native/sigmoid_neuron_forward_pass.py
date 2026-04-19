## Building a sigmoid neuron only , forward pass only

import numpy as np


class SigmoidNeuron:
    def __init__(self,weights,bias):
        self.weights = np.array(weights,dtype=float)
        self.bias = float(bias)
        
    def sigmoid(self,z):
        return 1/(1+np.exp(-z))
    
    def weighted_sum(self,x):
        x = np.array(x,dtype=float)
        return np.dot(self.weights,x) + self.bias
    
    
    def forward(self,x):
        z = self.weighted_sum(x)
        y_hat = self.sigmoid(z)
        print("z:\n",z)
        print("Prediction:\n",y_hat)
        return y_hat
        
        
if __name__=="__main__":
    model = SigmoidNeuron(
        weights = [0.5,0.5],
        bias = 0
        )
    model.forward([1,2])    
        
        