import numpy as np
import VariableDef as vdf
import Utility as util
from numpy import linalg as LA

def ProximalGradient(infoParser):
    # Parsing variable
    nablaf    = infoParser.nablaf

    tol       = infoParser.modelPara.tol
    maxiter   = infoParser.modelPara.maxiter 
    normType  = infoParser.modelPara.normType

    betaEst   = infoParser.data.betaEst
    y         = infoParser.data.y
    X         = infoParser.data.X

    lam       = infoParser.lam
    proxyOp   = infoParser.ProxyOp
    objeval   = infoParser.obj

    # temporary variables
    tk = 1 
    betaPrev = betaEst

    for i in range(0, maxiter):
        
        objPrev   = objeval(X, y, betaPrev, lam)
        # Backtracking line search (Armijo)
        while 1:
            grad_beta = nablaf(X, y, betaPrev)
            print(grad_beta)
            deltabeta = tk * grad_beta
            betaCand  = proxyOp(betaPrev - deltabeta, tk*lam)
            print(betaCand)
            objCand   = objeval(X, y, betaPrev - deltabeta, lam)
            
            #grad_x'*(z - x) + (1/(2*lambda))*sum_square(z - x)
            if objCand <= objPrev + np.inner(grad_beta, betaCand - betaPrev) +  1/(2*tk) * LA.norm(betaCand - betaPrev)**2:
                break
            else: 
                tk = tk/2

        if i > 1:         
            tau = LA.norm(objCand - objPrev)/LA.norm(ObjPrev) 

        if tau < tol :
            break
        beta_Prev = betaCand 


# test 
if __name__ == '__main__':
    # basic infomation
    ind_sparse = [0,1,2,3,4,5,15,16]
    seed = 101
    n = 100
    p = 20
    # Data_Generator returns a class with data structure with X,Y,betaEST and beta;
    dataTest = util.Data_Generator(n, p, ind_sparse, seed)
    
    # initialize modelPara structure
    modelp = vdf.modelPara()
    modelp.add('x0', np.zeros((p,1)))
    modelp.add('normType', '2')
    modelp.add('maxiter', 1000)
    modelp.add('tol', 1e-8)

    # initialize infoParser structure
    infoP = vdf.infoParser()
    infoP.add('modelPara', modelp)
    infoP.add('data', dataTest)
    infoP.add('nablaf', util.nablaf_Gaussian)
    infoP.add('lam', 0.5)
    infoP.add('ProxyOp', util.soft_Thresholding)
    infoP.add('obj', util.obj_gaussian)

    # set up initial value, parse the intial value from modelpara to data structure
    dataTest.betaEst = modelp.x0

    ProximalGradient(infoP)


    
    




