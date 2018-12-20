import numpy as np;

class FlatSigmoid():
    """Flattened Sigmoid. f(0)=.1, f(maxframes/2)=.5"""
    @staticmethod
    def __init__(self, maxframes):
        self.alpha = maxframes/2
        self.beta = alpha/np.log(9)

    def f(t):
        # shift by alpha, scale by beta
        return 1+ 1./2*(1.+np.exp(-(t-self.alpha)/self.beta))
