import numpy as np
import VariableDef as vdf
import Utility as util
from numpy import linalg as LA

def ProximalGradient(infoParser):
    # This is a demo solver for proximal gradient algorithm with line search for t
    # It aims to solve the problem with the following update
    # beta(k+1) = prox(beta(k) - t * nablaF(beta(k)))

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
    tau = float('inf') 
    betaPrev = betaEst
    objvec = np.zeros(maxiter)

    # main loop
    for i in range(0, maxiter):
        
        objPrev   = objeval(X, y, betaPrev, lam)
        # Backtracking line search 
        while 1:
            # compute gradient for previous beta
            grad_beta = nablaf(X, y, betaPrev)
            deltabeta = tk * grad_beta
            # proximal operator:
            betaCand  = proxyOp(betaPrev - deltabeta, tk*lam)
            # compute the obj based on current new beta
            objCand   = objeval(X, y, betaPrev - deltabeta, lam)
            #grad_x'*(z - x) + (1/(2*lambda))*sum_square(z - x)
            if objCand <= objPrev + np.inner(grad_beta.transpose(), (betaCand - betaPrev).transpose()) + 1/(2*tk) * LA.norm(betaCand - betaPrev)**2:
                break
            else: 
                tk = tk/2
        
        # store the obj value based on current beta for tracking purpose
        objvec[i] = objCand

        # convergence criterion:
        if i > 0:         
            tau = LA.norm(objCand - objPrev)/LA.norm(objPrev) 
        if tau < tol :
            break

        betaPrev = betaCand

    # outPut Summary 
    infoP.outPut.add('betaEst', betaCand)
    infoP.outPut.add('tau', tau)
    infoP.outPut.add('iter', i)
    infoP.outPut.add('obj', objvec[1:i])
    return(infoParser)


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

    # initialize the output structure
    outPut = vdf.outPut()

    # initialize infoParser structure
    infoP = vdf.infoParser()
    infoP.add('modelPara', modelp)
    infoP.add('outPut', outPut)
    infoP.add('data', dataTest)
    infoP.add('nablaf', util.nablaf_Gaussian)
    infoP.add('lam', 5)
    infoP.add('ProxyOp', util.soft_Thresholding)
    infoP.add('obj', util.obj_gaussian)

    # set up initial value, parse the intial value from modelpara to data structure
    dataTest.betaEst = modelp.x0

    # run the actual algorithm and show all
    beta = ProximalGradient(infoP)
    beta.showAll()


    
    




