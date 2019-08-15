import numpy as np;

class Generating_Function(object):
    """ Interface for a generating function.
    A Generating_Function must implement the __call__ method. """

    def __call__(self, t:int):
        """ Takes in the (integer) frame number (hence a time t).
        Outputs the probability to generate a bullet. """
        raise NotImplementedError("Call to the interface's method")


class FlatSigmoid(Generating_Function):
    """Flattened Sigmoid. f(0)=.1, f(maxframes/2)=.5"""
    def __init__(self, maxframes):
        self.alpha = maxframes/2;
        self.beta = self.alpha/np.log(9);

    def __call__(self,t:int):
        """ Probability w.r.t t is a flattened sigmoid.
        See __init__ for alpha&beta definitions """
        return 1 + 1./2*(1.+np.exp(-(t-self.alpha)/self.beta))
