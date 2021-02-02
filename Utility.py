import VariableDef as vdf
import random
import numpy as np
from numpy import linalg as LA

# Generate Pseudo Data For Testing Purpose:
def Data_Generator(n, p, ind_sparse, seed):
    # set seed
    np.random.seed(seed=seed)
    # design matrix
    X = np.random.normal(0, 1, (n, p))
    # noise term
    epsilon = np.random.normal(0, 1,(n, 1))
    beta = np.random.normal(0, 1, (p, 1))
    # sparse indices and create sparsity in the parameter vector
    for num in ind_sparse:
        beta[num] = 0
    # generate response variable
    y = np.matmul(X, beta) + epsilon
    # store result into data class, detail please see its definitions.
    data = vdf.data()
    data.add('X', X)
    data.add('y', y)
    data.add('beta', beta)
    return(data)

# Gaussian Gradient for 1/2|| y - Xbeta||_2^2 with respect to beta
def nablaf_Gaussian(X, y, betaEst):
    XT = X.transpose()
    r =  y - np.matmul(X, betaEst)
    v  = - np.matmul(XT, r)
    return(v)

# penalized l2 gaussian objective function with lambda.

def obj_gaussian(X, y, betaEst, lam):
    v = 0.5 * LA.norm(y - np.matmul(X, betaEst))**2 + lam * np.sum(np.abs(betaEst))
    return(v)

# soft thresholding = proximal operator for l1 norm
def soft_Thresholding(v, th):
    return(np.sign(v) * np.maximum(np.abs(v) - th, 0))

# test
if __name__ == '__main__':
    ind_sparse = [0,1,2,3,4,5,15,16]
    seed = 101
    n = 100
    p = 20
    Data = Data_Generator(n,p, ind_sparse, seed)
    print(Data.X)

