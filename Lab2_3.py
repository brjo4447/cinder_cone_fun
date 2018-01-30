"""
Created on Mon Jan 29 13:20:06 2018
Lab 2: cinder cone fun
@author: Brittany
"""

#Importing stuff
import numpy as np
import math, random #,sys,os,pandas,csv,itertools
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
D_max = 3 #max ejecta diameter (m)
D_mode = D_max/2 #mode of ejecta sizes (m)
alpha_max = 80
alpha_min = 0
t = 150000 #number of times a projectile is spit out
ventsize = 2 #in addition to 1 meter
x_size = 1 # size of x increment in meters (the dx bit)
angleofrepo=math.radians(35) #angle of repose in degrees
## Determining max grid size 
#velocities
umax = math.cos(math.radians(45)) * v_max
wmax = math.sin(math.radians(45)) *v_max

#max sizes given those velocities
zmax = (wmax**2)/(2*g)
xmax = (2*umax*wmax)/g 

#simple array
z_topo = np.zeros(shape =(int(round(xmax))))
xcols = range(np.size(z_topo))+[0]

for i in range(t):
    V = np.random.randint(v_min, high=v_max, size=None, dtype='l')#random velocity
    D = random.random()#(D_min, D_max,D_mode) #random diameter
    D2Z = (math.pi*(D**2))/(4*x_size) #size of projectile diameter to change in Z
    alpha = np.random.randint(alpha_min, high=alpha_max, size=None, dtype='l') #random alpha
    u0 = V * math.cos(math.radians(alpha)) # x velocity
    w0 = V * math.sin(math.radians(alpha))
    L = (2*u0*w0)/g
    z_topo[int(round(L))]= z_topo[int(round(L))] + D2Z
    angletopo = math.tan(math.radians((z_topo[int(round(L))] - z_topo[int(round(L))+3])/3)) #finding the angle of cone for 4 spaces to right
    if angletopo>=angleofrepo:
        z_topo[int(round(L))]= z_topo[int(round(L))] - D2Z
        d2z = D2Z/4
        z_topo[int(round(L))]= z_topo[int(round(L))]+d2z
        z_topo[int(round(L))+1]= z_topo[int(round(L))+1]+d2z
        z_topo[int(round(L))+2]= z_topo[int(round(L))+2]+d2z
        z_topo[int(round(L))+3]= z_topo[int(round(L))+3]+d2z
#        z_topo[int(round(L))+4]= z_topo[int(round(L))+4]+d2z
#        z_topo[int(round(L))+5]= z_topo[int(round(L))+5]+d2z
#        z_topo[int(round(L))+6]= z_topo[int(round(L))+6]+d2z
#        z_topo[int(round(L))+7]= z_topo[int(round(L))+7]+d2z
#        z_topo[int(round(L))+8]= z_topo[int(round(L))+8]+d2z
#        z_topo[int(round(L))+9]= z_topo[int(round(L))+9]+d2z
        z_topo[0:ventsize +1] = [(np.max(z_topo[2::]))/2]* (ventsize+1)
    else:
        z_topo[0:ventsize +1] = [(np.max(z_topo[2::]))/2]* (ventsize+1)

plt.plot(z_topo,'brown')



#
#
#
#
#
#
#
#for i in range(t):
#    V = np.random.randint(v_min, high=v_max, size=None, dtype='l')#random velocity
#    D = random.random()#(D_min, D_max,D_mode) #random diameter
#    D2Z = (math.pi*(D**2))/(4*x_size) #size of projectile diameter to change in Z
#    alpha = np.random.randint(alpha_min, high=alpha_max, size=None, dtype='l') #random alpha
#    u0 = V * math.cos(math.radians(alpha)) # x velocity
#    w0 = V * math.sin(math.radians(alpha))
#    L = (2*u0*w0)/g
#    #z_topo[int(round(L))]= z_topo[int(round(L))] + D2Z
#    #itemindex = np.where(z_topo==int(round(L))) #find where trajectory would land
#    #z_topo[itemindex]= z_topo[itemindex] + D2Z
#    z_traj = []
#    
#    for j in range(len(xcols)): #for every column
#        z_traj.append(z_topo[0]+(((w0*xcols[j])/u0)-((g*(xcols[j]**2))/(2*(u0**2))))) #create list of trajectories
#    z_topo_int=[z_topo.astype(int)]+[0]
#    z_traj_int = map(int, z_traj)
#    itemindex = next(index for index, value in enumerate(z_topo_int) if (value<=z_traj_int[1::]))
#    #itemindex= next(x for x in z_topo_int if x<=z_traj_int[1::])
#    #itemindex = np.where(z_topo_int<=z_traj_int[2::]) 
#    z_topo[itemindex]= z_topo[itemindex] + D2Z
#    z_topo[0:ventsize +1] = [(np.max(z_topo[2::]))/2]* (ventsize+1)    
#    
#    
##plt.plot(x, y)
#plt.plot(z_topo,'y--')
#
#
#
#
##method 2
#
##Creating variables
#g = 9.81 #gravity (m/s2)
#v_min = 5 #min velocity (m/s)
#v_max = 35 #max velocity (m/s)
#D_min = .001#min ejecta diameter (m)
#D_max = 1 #max ejecta diameter (m)
#D_mode = 0.5 #mode of ejecta sizes (m)
#alpha_max = 90
#alpha_min = 0
#t = 150000 #number of times a projectile is spit out
#ventsize = 2 #in addition to 1 meter
#x_size = 1 # size of x increment in meters (the dx bit)
#
### Determining max grid size 
##velocities
#umax = math.cos(math.radians(45)) * v_max
#wmax = math.sin(math.radians(45)) *v_max
#
##max sizes given those velocities
#zmax = (wmax**2)/(2*g)
#xmax = (2*umax*wmax)/g 
#
##simple array
#z_topo = np.zeros(shape =(int(round(xmax))))
#xcols = range(np.size(z_topo))+[0]
#
## D array
#D = np.zeros(shape =(t))
#for i in range(t):
#    D[i] = random.random()
##V array    
#V= np.zeros(shape =(t))
#for i in range(t):
#    V[i] = np.random.randint(v_min, high=v_max, size=None, dtype='l')
##alpha array
#alpha = np.zeros(shape =(t))
#for i in range(t):
#    alpha[i] = np.random.randint(alpha_min, high=alpha_max, size=None, dtype='l')
## size of projectile to z elevation array  
#D2Z = np.zeros(shape =(t))
#for i in range(t):
#    D2Z[i] = (math.pi*(D[i]**2))/(4*x_size) #size of projectile diameter to change in Z
##x velocity array
#u0=np.zeros(shape =(t))
#for i in range(t):
#    u0[i] = V[i] * math.cos(math.radians(alpha[i])) # x velocity
##y velocity array
#w0=np.zeros(shape =(t))
#for i in range(t):
#    w0[i] = V[i] * math.sin(math.radians(alpha[i])) # x velocity
#
#
#for i in range(t):
#    z_traj = []
#    z_traj_min = []
#    z_traj_max = []
#    for j in range(len(xcols)):
#        z_traj.append(z_topo[0]+(((w0*xcols[j])/u0)-((g*(xcols[j]**2))/(2*(u0**2)))))
#    z_traj_int = map(int, z_traj)
#    for k in range(len(z_traj)-1):
#        z_traj_min.append(z_traj_int[k]-z_traj_int[k+1])
#    itemindex = np.where(z_topo<=z_traj_int[2::]) 
#
#
#
######################
#    
#for i in range(t):
#    V = np.random.randint(v_min, high=v_max, size=None, dtype='l')#random velocity
#    D = random.random()#(D_min, D_max,D_mode) #random diameter
#    D2Z = (math.pi*(D**2))/(4*x_size) #size of projectile diameter to change in Z
#    alpha = np.random.randint(alpha_min, high=alpha_max, size=None, dtype='l') #random alpha
#    u0 = V * math.cos(math.radians(alpha)) # x velocity
#    w0 = V * math.sin(math.radians(alpha))
#    L = (2*u0*w0)/g
#    #z_topo[int(round(L))]= z_topo[int(round(L))] + D2Z
#    #itemindex = np.where(z_topo==int(round(L))) #find where trajectory would land
#    #z_topo[itemindex]= z_topo[itemindex] + D2Z
#    z_traj = []
#    
#    for j in range(len(xcols)): #for every column
#        z_traj.append(z_topo[0]+(((w0*xcols[j])/u0)-((g*(xcols[j]**2))/(2*(u0**2))))) #create list of trajectories
#    z_topo_int=z_topo.astype(int)
#    z_traj_int = map(int, z_traj)
#    itemindex = np.where(z_topo_int<=z_traj_int[2::]) 
#    z_topo[itemindex]= z_topo[itemindex] + D2Z
#    z_topo[0:ventsize +1] = [(np.max(z_topo[2::]))/2]* (ventsize+1)    
#    
#    
##plt.plot(x, y)
#plt.plot(z_topo,'y--')
#
#fig, ax1 = plt.subplots()
#ax1.plot(z_topo,'y--')
#
#
#
#
#
#
##ax1.plot(elev_max,'y--')
##ax1.plot(elev_ave,'y-')
##ax1.tick_params('b', colors='y')
#
#ax2 = ax1.twinx()
#ax2.plot(percent_rockcover,'b')
#ax2.plot(percent_veg,'g--')
#ax2.tick_params('r', colors='r')
#
#ax1.set_xlabel('Distance (m)')
##ax1.set_ylabel('Elevation (m)', color='y')
#ax1.set_ylabel('Channel Elevation (m)', color='y')
#ax2.set_ylabel('Rock Cover Percent', color='b')
##ax2.set_ylabel('Vegetation Percent', color='g')
#
#
##plt.legend(['min', 'max', 'average','Rock Cover'], loc='upper left')
#fig.tight_layout()
#plt.show()
#    
#test = np.zeros(shape=(3,2))
#test = np.array([0, 2, 3,1,4,5,6])
#test2 = [0, 1, 3,4,5,6,7]
#
#itemindex = np.where(test==test2)
#np.amin(test) 
#
#x = np.amin(test[2::]) 
#test2[0:ventsize +1] = [np.amin(test[2::])]* (ventsize+1)
