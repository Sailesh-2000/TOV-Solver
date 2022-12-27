import numpy as np

def Lamda(m,r):
    
    lamda = -(np.log(1-(2*m/r)))/2
    
    return lamda