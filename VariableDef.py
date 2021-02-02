import numpy as np

# variable definition
class modelPara:
    def __init__(self):
        self.x0       = []
        self.model    = []
        self.normType = []
        self.maxiter  = []
        self.tol      = []
    def add(self, name, parm):
        setattr(self, name, parm) # self.name = par doesnt work. related to string, attribute and variable issues
    def showAll(self):
        for attribute, value in self.__dict__.items():
            print(attribute, '=', value)

class data:
    def __init__(self):
        self.y = []
        self.X = []
        self.beta = []
        self.betaEst = []
    def add(self, name, parm):
        setattr(self, name, parm)
    def scaleX(self):
        self.X = scale(X)
    def showAll(self):
        for attribute, value in self.__dict__.items():
            print(attribute, '=', value)

class infoParser:
    def __init__(self):
        self.modelPara = []
        self.data      = []
        self.nablaf    = []
        self.obj       = []
        self.lam       = []
        self.ProxyOp   = []
    def add(self, name, parm):
        setattr(self, name, parm)
    def showAll(self):
        for attribute, value in self.__dict__.items():
            print(attribute, '=', value) 

if __name__ == '__main__':
    points = np.matrix([
        [1.,2.,3.],   # 1st point
        [4.,5.,6.]]   # 2nd point
    )