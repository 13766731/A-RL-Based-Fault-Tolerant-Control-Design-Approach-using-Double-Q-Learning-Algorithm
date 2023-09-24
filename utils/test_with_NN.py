# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 00:33:18 2020

@author: a.h
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 00:19:57 2020

@author: a.h
"""

######################################### IMPORTS ##################################################

import numpy as np
from CSTR_plant import CSTR_plant
import random
from PID_controller import PID_controller
import  matplotlib.pyplot as plt
from State import State
from Reward import Reward
from Policy import Policy
from Enter_state import Enter_state
from Q_Learning_Algorithm import Q_Learning_Algorithm
from Duble_Q_Learning import Duble_Q_Learning
from pybrain.tools.customxml.networkreader import NetworkReader
from NN_CSTR import NN_CSTR

################################################# PARAMETERS ##################################

actions=list(range(-3,4)) 
state=list(range(0,11))
y_out = np.zeros(2000)
m = np.zeros(2000)
error_mse= np.zeros(2000)
loop_circle=0
error = 0
fault = 0#random.randint(-5,5)
a=0
yy =0
mean_duble=np.zeros(100)
ii =0

################################################### MAIN LOOP #######################################

while loop_circle <2000:
    if loop_circle == 0:
        y_out[loop_circle] = NN_CSTR(1)
        error_mse[loop_circle] = (1 - y_out[loop_circle])**2
               
    else:
        if loop_circle <= 1000:
                control_action = PID_controller(NN_CSTR,y_out[loop_circle])
                y_out[loop_circle] = NN_CSTR(control_action)
                error_mse[loop_circle] = (1 - y_out[loop_circle])**2
               
                

        if loop_circle > 1000 and a==0:

              if abs(error)<= 0.0 and a==0 :
               
                control_action = PID_controller(NN_CSTR,y_out[loop_circle])
                y_out[loop_circle] = NN_CSTR(control_action)+fault
                error_mse[loop_circle] = (1 - y_out[loop_circle])**2
                
                
                
              else: 
                print('ya abolfazlllllleeeeee')
                state = Enter_state(error)      
                print('state',state)  
                # (A,y_out,loop_circle,loop_Q_Learning,error_mse) = Q_Learning_Algorithm (fault,state,State,Reward,Policy,CSTR_plant,loop_circle,y_out,error_mse)
                # a=1
                (A,y_out,loop_circle,loop_Q_Learning,error_mse) = Duble_Q_Learning(fault,state,State,Reward,Policy,NN_CSTR,loop_circle,y_out,error_mse)
                a=1
                
                
        if loop_circle > 1000 and a==1:
            y_out[loop_circle] = NN_CSTR(A) + fault
            error_mse[loop_circle] = (1 - y_out[loop_circle])**2

                   
    error =   1 - y_out[loop_circle]
    loop_circle += 1
    print(loop_circle)
    #print(loop_circle)

    
        


##################################### PLOT ##############################

t=np.linspace(0,100,2000)        
plt.figure(1)
plt.plot(t,y_out[0:2000])  
mse = 0
for e in range(np.size(error_mse)):
    mse += error_mse[e]
MSE = mse / np.size(error_mse)
print('MSE is :   ')
print(MSE)
