## Explain the complete backpropogation

import numpy as np
from numpy.typing import NDArray


class Neuron:
    def __init__(self,weights,bias):
        self.weights = np.array(weights,dtype=float)
        self.bias = float(bias)
    
    def sigmoid(self,z):
        return 1/(1+np.exp(-z))
        
    def mse_loss(self,y_pred,y_true):
        result = 0.5*(y_pred,y_true)**2
        return result
    
    def forward(self,input):
        input = np.array(input,dtype=float)
        z = np.dot(self.weights,input) + self.bias
        y_pred = self.sigmoid(z)
        return z,y_pred
    
    def backward(self,input,y_true):
        input = np.array(input, dtype=float)
        z,y_pred = self.forward(input)
        
        # Errror calculation
        error = (y_pred-y_true)
        sigmoid_derivative  = (y_pred*(1-y_pred))
        
        
        # Bias gradient  
        dl_db = (error * sigmoid_derivative)
        
        
        # weight gradient
        dl_dw = (dl_db*input)
        
        
        ## rounding of all the gradients
        dl_dw = np.round(dl_dw,5)
        dl_db = np.round(float(dl_db),5)
        
        
        return (dl_dw,dl_db)
        
        
        
if __name__=="__main__":
    input = [1.0,2.0]
    w = [0.5,0.5]
    b = 0.0
    y_true = 1.0
    neuron = Neuron(w,b)
    grads = neuron.backward(input,y_true)
    print(grads)
        
        
        
        