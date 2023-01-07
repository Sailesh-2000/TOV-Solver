import numpy as np
from scipy.interpolate import interp1d

from .Constants import *

def EOS_Data(path):
    
    Data = np.loadtxt(path)
    e= Data[:,1]*Mev_per_fm_cube__to__Pa*Pa__to__per_m_square
    p= Data[:,2]*Mev_per_fm_cube__to__Pa*Pa__to__per_m_square
    
    Data= [Data[:,1],Data[:,2]]

    min_p= np.min(p)
    max_p= np.max(p)
    min_e= np.min(e)
    max_e= np.max(e)
    
    CP= [min_p,max_p,min_e,max_e]

    P2E= interp1d(p, e)
    E2P= interp1d(e, p)
    
    EOS= P2E, E2P
    
    return Data, CP, EOS