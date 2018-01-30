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

Note to self:
np.zeros(shape=(rows,columns))
np.zeros(shape=(z,x))

range(np.size(a,1)): #for every column say i
range(np.size(a,0)): #for every row say j
a[j,i]
a[row,column]    
    
'''
#Creating variables
g = 9.81 #gravity (m/s2)
v_min = 5 #min velocity (m/s)
v_max = 35 #max velocity (m/s)
D_min = .001#min ejecta diameter (m)
D_max = 1 #max ejecta diameter (m)
alpha_max = 0
alpha_min = 90
t = 150000 #number of times a projectile is spit out
ventsize = 2 #in addition to 1 meter

## Determining max grid size 
#velocities
umax = math.cos(45) * v_max
wmax = math.sin(45) *v_max

#max sizes given those velocities
zmax = (wmax**2)/(2*g)
xmax = (2*umax*wmax)/g 

#creating list of x values with vent
#matrix way
#z_topo = np.zeros(shape=(int(round(zmax,0)),int(round(xmax,0))))
#xcols = range(np.size(z_topo,1))
#xcols2 = xcols[-1] -ventsize+1
#xcols = range(xcols2)
#listofzeros = [0] * ventsize
#xcols = listofzeros + xcols
#

#simple array
z_topo = np.zeros(shape =(int(round(xmax))))
xcols = range(np.size(z_topo))
xcols2 = xcols[-1] -ventsize+1
xcols = range(xcols2)
listofzeros = [0] * ventsize
xcols = listofzeros + xcols


t = 2
for i in range(len(t)):
    V = np.random.randint(v_min, high=v_max, size=None, dtype='l')#random velocity
    D = np.random.randint(D_min, high=D_max, size=None, dtype='l') #random diameter
    D2Z = (math.pi*(D**2))/4
    alpha = np.random.randint(alpha_min, high=alpha_max, size=None, dtype='l') #random alpha
    u0 = V * math.cos(alpha) # x velocity
    w0 = V * math.sin(alpha)
    L = (2*u0*w0)/g
    z_traj = []
    for j in range(len(xcols)): #for every column
        z_traj.append(((w0*xcols[j])/u0)-((g*(xcols[j]**2))/(2*u0))) #create list of trajectories
    itemindex = np.where(z_topo==z_traj) 
    z_topo[itemindex]= z_topo[itemindex] 
    
    
test = np.zeros(shape=(3,2))
test = np.array([1, 2, 3])
test2 = [0, 1, 3]

itemindex = np.where(test==test2)    
