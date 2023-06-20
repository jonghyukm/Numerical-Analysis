import numpy as np                                      #numpy import
import matplotlib.pyplot as plt                         #pyplot import

t=np.linspace(0,1,1001)                                 #set time
dt=0.001                                                #set step size
x1=np.zeros(len(t))                                     #for Euler method
x1[0]=1                                                 #set initial condition
for i in range(len(t)-1):                               #iteration
    x1[i+1]=x1[i]+dt*(1+2*t[i]*x1[i]-((x1[i])**2)/2)    #Use Euler Method
plt.figure                                              #Make figure
plt.plot(t,x1)                                          #plot x1
plt.title("Euler's Method")                             #title of this plot
plt.show()                                              #show plot

x2=np.zeros(len(t))                                     #for Heun's Method
x2[0]=1                                                 #set initial condition
for i in range(len(t)-1):                               #iteration
    temp=x2[i]+dt*(1+2*t[i]*x2[i]-((x2[i])**2)/2)       #save value temporarily
    x2[i+1]=x2[i]+0.5*dt*((1+2*t[i]*x2[i]-((x2[i])**2)/2)
                       +(1+2*t[i]*temp-((temp)**2)/2))  #Use Heun's Method
plt.figure                                              #Make figure
plt.plot(t,x2)                                          #plot x2
plt.title("Heun's Method")                              #title of this plot
plt.show()                                              #show plot

x3=np.zeros(len(t))                                     #for Runge-Kutta
x3[0]=1                                                 #set initial condition
for i in range(len(t)-1):                               #iteration
    temp=x3[i]+dt*(1+2*t[i]*x3[i]-((x3[i])**2)/2)       #save value temporarily
    x3[i+1]=x3[i]+dt*((1/3)*(1+2*t[i]*x3[i]-((x3[i])**2)/2)
                 +(2/3)*(1+2*t[i]*temp-((temp)**2)/2))  #Use Runge-Kutta Method
plt.figure                                              #Make figure
plt.plot(t,x3)                                          #plot x3
plt.title("Runge-Kutta's Method")                       #title of this plot
plt.show()                                              #show plot