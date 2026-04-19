# building percepton from scratch

import numpy as np

class Perceptron:
    def __init__(self,weights,bias):
        self.weights = np.array(weights,dtype=float)
        self.bias = float(bias)
    
    # step function
    """Here step function is used as an activation function, it will convert the output of the weighted sum into binary output (0 or 1) based on a threshold (in this case, 0). If the weighted sum is greater than or equal to 0, the step function will return 1; otherwise, it will return 0."""
    def step_function(self,z):
        if z>=0:
            return 1
        return 0
    
    # weighted sum
    def weighted_sum(self,inputs):
        inputs = np.array(inputs,dtype=float)
        return np.dot(self.weights,inputs)+ self.bias
    
    # forward
    def forward(self,inputs):
        z = self.weighted_sum(inputs)
        output = self.step_function(z)
        print("Weighted Sum:\n",z)
        print("Prediction:\n",output)
        return output
        
if __name__=="__main__":
     p = Perceptron(weights = [1,-1],bias=0)
     p.forward([2,3])
    
    