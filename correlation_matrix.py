import numpy as np

A = np.array([[1,2],[3,4]])
B = np.array([[2,4],[6,8]])

# Now Flatten the array

X = A.flatten()
Y = B.flatten()


# finding the correlation

corr = np.corrcoef(X,Y)[0,1]
print("Correlation : ",corr)

## when the value is near 1 , then it shows the linear relationship
# Correlation = 1 → perfectly aligned patterns
# Correlation = 0 → no relationship
# Correlation = -1 → opposite patterns