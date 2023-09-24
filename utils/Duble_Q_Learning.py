# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 00:02:50 2020

@author: a.h
"""

def Duble_Q_Learning(fault,state,State,Reward,Policy,CSTR_plant,loop_circle,y_out,error_mse):
    import random
    import numpy as np
    actions11=list(range(-3,4)) 
    state11=list(range(0,11))
    loop_Q_Learning = 0
    alpha=0.1 #float(input('Enter alpha:   '))
    gama=0.9 # float(input('Enter gama:   '))
    epsilon = 0.1
    Reward_Q = np.zeros(300)
    # Q1=np.random.rand(np.size(state11),np.size(actions11))
    # Q1[0,:]=0
    # Q2=np.random.rand(np.size(state11),np.size(actions11))
    # Q2[0,:]=0
    Q1=np.zeros((np.size(state11),np.size(actions11))) 
    Q2=np.zeros((np.size(state11),np.size(actions11))) 
    while state >0 :
        A = Policy((Q1+Q2),state,epsilon)
        S_perim = State(A,fault,CSTR_plant)
        R = Reward(S_perim)
        Reward_Q [loop_circle] = sum((sum(abs(Q1) + abs(Q2))))/2
        if random.uniform(0, 1) < 0.5:
            print(state)
            Q1[state,A] = Q1[state,A] + alpha * (R + gama * Q2[S_perim,round(max(Q1[S_perim,:]))]-Q1[state,A])
        else:
            Q2[state,A] = Q2[state,A] + alpha * (R + gama * Q1[S_perim,round(max(Q2[S_perim,:]))]-Q2[state,A])
        
        state = S_perim
        y_out[loop_circle] = CSTR_plant(A) + fault
        error_mse[loop_circle] = (1 - y_out[loop_circle])**2
        loop_Q_Learning += 1
        loop_circle += 1
    return (A,y_out,loop_circle,loop_Q_Learning,error_mse,Reward_Q)
    