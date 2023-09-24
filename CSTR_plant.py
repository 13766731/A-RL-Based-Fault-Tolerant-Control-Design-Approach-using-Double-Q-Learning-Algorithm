# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 00:31:51 2020

@author: a.h
"""



def CSTR_plant(u) :
    import numpy as np
    from scipy import signal
    import matplotlib.pyplot as plt
    from scipy.integrate import odeint
    Kp = 5
    taup = 2.5
    def model3(y,t):
        return (-y + Kp * u)/taup
    
    t= np.linspace(0,1,100)
    y_plant = odeint(model3,0,t)
    return  (y_plant[99])/10 
    
    
 

    
    
    
    
    
    
    
    
    
    