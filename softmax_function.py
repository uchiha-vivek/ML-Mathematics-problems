import numpy as np


def softmax(x):
    exp_x = np.exp(x)
    result  = exp_x/ np.sum(exp_x)
    return result
    

## implementing stable softmaxn functions
def stable_softmax(x):
    x = x - np.max(x)
    exp_x = np.exp(x)
    return exp_x/ np.sum(exp_x)
    

if __name__=="__main__":
    x = np.array([2.0,1.0,0.1])
    # print(softmax(x))
    print(stable_softmax(x))