# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 11:09:09 2020

@author: Kwame Anokurang-Budu
"""

import numpy as np
import scipy.optimize as sp

n_eth = 98570.636 #mol
n_ace = 5187.928 #mol

R = 0.08205
T = 270
P = 22.7

a_eth = 4.547
a_ace = 4.453

b_eth = 0.05821
b_ace = 0.0522


#defining fuctions for eth. and ace. volume:

def Eth(init_eth):
    V = init_eth[0]
    Fv = (n_eth*R*T)/(V-n_eth*b_eth) - (n_eth**2*a_eth)/(V**2) - P
    
    return Fv

def Ace(init_ace):
    V = init_ace[0]
    Fv = (n_ace*R*T)/(V-n_ace*b_ace) - (n_ace**2*a_ace)/(V**2) - P
    
    return Fv

#Initial vaules for volume of eth. and ace. in list format

eth_guess = [96197]
ace_guess = [5053]

'''
Function test
FE = Eth(eth_guess)
FA = Ace(ace_guess)
'''

#putting both functions and their initial guess lists into solver

V_eth = sp.fsolve(Eth,eth_guess)
V_ace = sp.fsolve(Ace,ace_guess)


#printing results
Total_vol = "{:.3f}".format(V_eth[0] + V_ace[0])

V_eth = "{:.3f}".format(V_eth[0])
V_ace = "{:.3f}".format(V_ace[0])



print("The volume of Ethylene is",V_eth,"L")
print("The volume of Acetylene is" , V_ace,"L")
print("The total volume of the tank is",Total_vol,"L")