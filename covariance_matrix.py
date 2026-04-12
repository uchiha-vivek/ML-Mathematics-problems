## Finding covariance matrix
import numpy as np

X = np.array([[1,2],[3,4],[5,6]])

cov_matrix = np.cov(X, rowvar=False)

print("Covariance Matrix:\n",cov_matrix)


# Used heavily in:
# Portfolio risk (covariance matrix of assets)
# PCA (principal component analysis)
# Multivariate statistics