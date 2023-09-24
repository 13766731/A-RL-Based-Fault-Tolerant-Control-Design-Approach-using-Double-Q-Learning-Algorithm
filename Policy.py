# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 11:28:56 2020

@author: a.h
"""

def Policy(Q,S,epsilon):
    import random
    if random.uniform(0, 1) < epsilon:
        A=random.randint(-3,3)
        return A
    else:
      for ii in range(7):
        a=Q[S,ii]
        b=max(Q[S,:])
        if  a >= b:
            A=ii
            return A-3