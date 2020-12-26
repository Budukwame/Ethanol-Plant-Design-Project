# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 14:26:14 2020

@author: Kwame Anokurang-Budu
"""

import numpy as np
import scipy.optimize as sp

#[dia. guess, ht. guess]
init_dim = [5.412,5.412]

#Tank Volume function
def TankDim(init_dim):
    D = init_dim[0]
    H = init_dim[1]
    
    F_v = ((np.pi*(D**3.))/6.) + (np.pi*((D/2.)**2.)*(1.4*D)) -83.264
    F_r = (H/D)-1.4
    
    return F_v,F_r


#putting function and guess list into solver
D,H =sp.fsolve(TankDim,init_dim)


#formatting and printing results
D = "{:.2f}".format(D)
H = "{:.2f}".format(H)

print("The Diameter of the Tank is", D , "m")
print("The Height of the Tank is", H ,"m")
    
    