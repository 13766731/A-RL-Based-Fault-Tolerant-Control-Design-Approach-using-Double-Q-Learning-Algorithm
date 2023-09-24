
import numpy as np
from pybrain.tools.customxml.networkreader import NetworkReader
import random 
actions=list(range(-3,4)) 
state=list(range(0,11))
y_out = np.zeros(100)
m = np.zeros(2000)
error_mse= np.zeros(100)
loop_circle=0
error = 0
fault = random.randint(-5,5)
a=0
yy =0
mean_duble=np.zeros(100)
ii =0
CSTR = NetworkReader.readFrom('CSTR.xml') 