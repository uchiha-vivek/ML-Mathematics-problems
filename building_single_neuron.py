# Building the single neuron
import numpy as np
class Neuron :
    def __init__(self,weights, bias):
        self.weights = np.array(weights,dtype=float)
        self.bias = float(bias)
    
    def sigmoid(self,z):
        """
        Activation function
        """
        return 1/(1+np.exp(-z))
    
    def weighted_sum(self,inputs):
        # z = w.x + b
        inputs = np.array(inputs,dtype=float)
        result = np.dot(self.weights,inputs) + self.bias
        return result
    
    def forward(self,inputs):
        """forward pass"""
        z = self.weighted_sum(inputs)
        output = self.sigmoid(z)
        return output
        
        
if __name__=="__main__":
    x = [1.0,2.0]
    w = [0.5,0.5]
    b = 0.0
    neuron = Neuron(w,b)
    result = neuron.forward(x)
    print(result)
