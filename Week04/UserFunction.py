import numpy as np

def Gauss(x, mu=0., sigma=1.):
    return 1./np.sqrt(2*np.pi)/sigma*np.exp(-0.5*(x-mu)**2/sigma**2)
