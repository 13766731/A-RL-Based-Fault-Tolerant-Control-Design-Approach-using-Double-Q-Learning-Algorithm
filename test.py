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
from numpy import savetxt

CSTR = NetworkReader.readFrom('CSTR.xml') 

################################################# PARAMETERS ##################################

actions=list(range(-3,4)) 
state=list(range(0,11))
y_out = np.zeros(100)
m = np.zeros(2000)
error_mse= np.zeros(100)
loop_circle=0
error = 0
fault = 1#random.randint(-5,5)
a=0
yy =0
mean_duble=np.zeros(100)
ii =0

################################################### MAIN LOOP #######################################

while loop_circle < 100:
    if loop_circle == 0:
        y_out[loop_circle] = CSTR_plant(1)
        error_mse[loop_circle] = (1 - y_out[loop_circle])**2
               
    else:
        if loop_circle <= 10:
                control_action = PID_controller(CSTR_plant,y_out[loop_circle])
                y_out[loop_circle] = CSTR_plant(control_action)
                error_mse[loop_circle] = (1 - y_out[loop_circle])**2
               
                

        if loop_circle > 10 and a==0:

              if abs(error)<= 0.2 and a==0 :
               
                control_action = PID_controller(CSTR_plant,y_out[loop_circle])
                y_out[loop_circle] = CSTR_plant(control_action)+fault
                error_mse[loop_circle] = (1 - y_out[loop_circle])**2
                
                
                
              else: 
                print('ya abolfazlllllleeeeee')
                state = Enter_state(error)      
                print('state',state)  
                (A,y_out,loop_circle,loop_Q_Learning,error_mse) = Q_Learning_Algorithm (fault,state,State,Reward,Policy,CSTR_plant,loop_circle,y_out,error_mse)
                # a=1
                # (A,y_out,loop_circle,loop_Q_Learning,error_mse) = Duble_Q_Learning(fault,state,State,Reward,Policy,CSTR_plant,loop_circle,y_out,error_mse)
                print(y_out)
                print('looooooppppp',loop_circle)
                a=1
               # 
                mean_duble[ii]=loop_Q_Learning
                
        if loop_circle > 10 and a==1:
            y_out[loop_circle] = CSTR_plant(A) + fault
            error_mse[loop_circle] = (1 - y_out[loop_circle])**2

                   
    error =   1 - y_out[loop_circle]
    loop_circle += 1
   
    print(loop_circle)
    #print(loop_circle)

    
        


##################################### PLOT ##############################

t=np.linspace(0,100,100)        
plt.figure(1)
plt.plot(t,y_out[0:100])  
mse = 0
for e in range(np.size(error_mse)):
    mse += error_mse[e]
MSE = mse / np.size(error_mse)
print('MSE is :   ')
print(MSE)
################################### save data for plotting ###################

# savetxt('PId_Q1.csv', y_out, delimiter=',')











