# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 11:26:54 2020

@author: a.h
"""

def Reward(state_now):
    if state_now == 0:
        R=1
    if state_now != 0:
        R=-1
    if (state_now >3):  #or  (state_now < -4):
        print('We are in Danger area')
        R=-100
        
    return R

