import numpy as np                              #import numpy
import matplotlib.pyplot as plt                 #import pyplot
m=1;l=1;T=0.1;g=9.8                             #set parameters
t=np.linspace(0,1,1001)                         #set time
dt=0.001                                        #set step size
A=np.array([[0,1],[-(g/l),0]])                  #set Matrix A with linearization
B=np.array([[0*T],[1*T/m*(l**2)]])              #set Matrix B
x1=np.zeros((2,len(t)))                         #values calculated by iteration will be saved here
x2=np.zeros((2,len(t)))                         #values calculated by iteration will be saved here
x1[0,0]=0.0001;x2[0,0]=0.0001                   #set initial conditions

for i in range(len(t)-1):                           #iteration
    x1[:,i+1:i+2]=x1[:,i:i+1]+dt*(A@x1[:,i:i+1]+B)  #Use Euler Method 
      
for i in range(len(t)-1):                           #iteration
    A[1,0]=-(g/l)*np.sin(x2[0,i:i+1])/x2[0,i:i+1]   #change matrix A, A is now matrix of non-linear equation
    x2[:,i+1:i+2]=x2[:,i:i+1]+dt*(A@x2[:,i:i+1]+B)  #Use Euler Method
    
def plotting(t,x,title):                            #define function
    plt.figure()                                    #Make figure
    plt.plot(t,x[0,:],label="θ(t)")                 #plot x's first row vector = θ(t)
    plt.title("Graph of θ(t) "+title)               #title of this plot
    plt.figure()                                    #Make figure
    plt.plot(t,x[0,:],label="θ(t)")                 #plot x's first row vector = θ(t)
    plt.plot(t,x[1,:],label="θ'(t)")                #plot x's second row vector = θ'(t)
    plt.title("Graph of Vector Θ "+title)           #set title
    plt.legend()                                    #show legends
    plt.show()                                      #show plots
plotting(t,x1,"linearized")                         #use plotting
plotting(t,x2,"without linearization")              #use plotting