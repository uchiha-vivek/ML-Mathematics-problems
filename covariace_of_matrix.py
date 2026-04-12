## finding the covariance of the matrix
# It measures how two variables change together:

# Positive → increase together
# Negative → one increases, other decreases
# Zero → no linear relation

# Cov(X,Y)=n−11​∑i=1n​(xi​−xˉ)(yi​−yˉ​)


import numpy as np

A = np.array([[1,2],[3,4]])
B = np.array([[2,0],[1,5]])

X = A.flatten()
Y = B.flatten()

cov = np.cov(X,Y)[0,1]

print("covariance :",cov)


