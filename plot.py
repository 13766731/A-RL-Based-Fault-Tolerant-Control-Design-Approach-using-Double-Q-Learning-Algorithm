# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 20:46:20 2020

@author: a.h
"""

from numpy import loadtxt
import  matplotlib.pyplot as plt
import numpy as np


pid_alon = loadtxt('PId_alone.csv', delimiter=',')
pid_Q1 = loadtxt('PId_Q1.csv', delimiter=',')
pid_Q2 = loadtxt('PId_Q2.csv', delimiter=',')
t=np.linspace(0,100,100)  
optimal_output = np.ones(100)
optimal_output[0] = 0


############################################## plot ########################################

plt.figure(1)
plt.plot(t,pid_alon)
plt.plot(t,optimal_output,'--')
plt.xlabel('time')
plt.ylabel('Concentrations A (CA)')
plt.legend(['Closed-loop with PID-Controller','optimal output'])
plt.show()


plt.figure(2)
plt.plot(t,pid_alon)
plt.plot(t,optimal_output,'.')
plt.plot(t,pid_Q1,'--')
plt.xlabel('time')
plt.ylabel('Concentrations A (CA)')
plt.legend(['Closed-loop with PID-Controller','optimal output','Closed-loop with CQLC'])
plt.show()


plt.figure(3)
plt.plot(t,pid_Q2)
plt.plot(t,pid_Q1,'--')
plt.xlabel('time')
plt.ylabel('Concentrations A (CA)')
plt.legend(['Closed-loop with DQLC','Closed-loop with CQLC'])
plt.show()





