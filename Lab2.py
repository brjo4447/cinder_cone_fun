"""
Created on Mon Jan 29 13:20:06 2018
Lab 2: cinder cone fun
@author: Brittany
"""

#Importing stuff
import numpy as np
import math#,sys,os,pandas,csv,itertools
import os
import csv
import matplotlib.pyplot as plt


'''
Notes
Velocity ranges are :
Angle ranges are :
Ejecta sizes are : 
Assume 45 degree angle is fastes w
    
'''
#Creating variables
g = 9.81 #gravity (m/s2)
v_min = 5 #min velocity (m/s)
v_max = 35 #max velocity (m/s)
D_min = .001#min ejecta diameter (m)
D_max = 1 #max ejecta diameter (m)
alpha_max = 0
alpha_min = 90
t = 150000 #time step

#Determining grid size
umax = math.cos(45) * v_max
wmax = math.sin(45) *v_max

zmax = (wmax**2)/(2*g)
xmax = (2*umax*wmax)/g 

#np.zeros(shape=(rows,columns))
#np.zeros(shape=(z,x))

z_topo = np.zeros(shape=(int(round(zmax,0)),int(round(xmax,0))))



#random veolocities
numpy.random.randint(low, high=None, size=None, dtype='l')
np.random.randint(1, high=10, size=None, dtype='l')


for i in range(len(t)):
    V = #random velocity
    D = #random diameter