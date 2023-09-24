# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 00:13:56 2020

@author: a.h
"""

def NN_CSTR(inpute):
    from pybrain.tools.customxml.networkreader import NetworkReader
    CSTR = NetworkReader.readFrom('CSTR.xml') 
    input_NN = inpute - 0.9721033157303889
    y_out = CSTR.activate([input_NN])
    y_NN = y_out + 0.16019707599775396
    return(y_NN)


