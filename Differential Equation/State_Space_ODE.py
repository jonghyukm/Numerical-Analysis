import numpy as np                          #import numpy         
import matplotlib.pyplot as plt             #import pyplot

t=np.linspace(0,1,1001)                     #set time
A=np.array([[0,1,0,0],[0,0,1,0],[0,0,0,1],[-4.5,-3.5,-2.5,-0.5]])   #set matrix A
B=np.array([[0],[0],[0],[-3]])              #set matrix B
x1=np.zeros((4,len(t)))                     #values calculated by iteration will be saved here
dt=0.001                                    #step size
x1[:,0]=np.array([0.1,0.2,0.3,0.5])         #set initial condition
for i in range(len(t)-1):                   #iteration
    x1[:,i+1:i+2]=x1[:,i:i+1]+dt*(A@x1[:,i:i+1]+B)  #Use Euler Method

plt.figure()                                #Make figure
plt.plot(t,x1[0,:])                         #plot x1's first row vector = x(t)
plt.title("Graph of x(t)")                  #set title
plt.figure()                                #Make figure
plt.plot(t,x1[0,:],label="x(t)")            #plot x1's first row vector = x(t)
plt.plot(t,x1[1,:],label="x'(t)")           #plot x1's second row vector = x'(t)
plt.plot(t,x1[2,:],label="x''(t)")          #plot x1's third row vector = x''(t)
plt.plot(t,x1[3,:],label="x'''(t)")         #plot x1's fourth row vector = x'''(t)
plt.title("Graph of vector X")              #set title
plt.legend()                                #plot legends
plt.show()                                  #show plots