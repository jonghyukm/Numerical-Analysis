import numpy as np                                  #numpy np라는 이름으로 호출
from matplotlib import pyplot as plt                #matplotlib의 pyplot plt라는 이름으로 호출
x=np.linspace(-5,25,100)                            #x는 linspace를 활용 100개의 point 저장
f=(1/np.sqrt(50*(np.pi)))*(np.exp((-(x-10)**2)/50)) #f는 주어진 수식

###Forward Method###
ff1=np.zeros(99)
for i in range(99):                                 #99회 반복
    ff1[i]=(f[i+1]-f[i])/(x[i+1]-x[i])              #ff1의 i번째에 Forward Method 수행한 값 저장
plt.figure()                                        #figure 생성
plt.plot(x[:-1],ff1)                                #x축을 x[:-1], y축을 ff1으로 하여 plot
plt.xlim(-5,25)                                     #x축을 -5부터 25까지로 제한
plt.xlabel("x")                                     #x축의 이름을 'x'로 설정
plt.ylabel("y")                                     #y축의 이름을 'y'로 설정
plt.title("Forward Method")                         #figure의 제목을 'Forward Method'로 설정
plt.show()                                          #plot 시행

###Backward Method###
ff2=np.zeros(99)                                    #차분 값을 저장할 ff2를 선언
for i in range(1,100):                              #99회 반복
    ff2[i-1]=(f[i]-f[i-1])/(x[i]-x[i-1])            #ff2의 i-1번째에 Backward Method 수행한 값 저장
plt.figure()                                        #figure 생성
plt.plot(x[:-1],ff2)                                #x축을 x[:-1], y축을 ff2으로 하여 plot
plt.xlim(-5,25)                                     #x축을 -5부터 25까지로 제한
plt.xlabel("x")                                     #x축의 이름을 'x'로 설정
plt.ylabel("y")                                     #y축의 이름을 'y'로 설정
plt.title("Backward Method")                        #figure의 제목을 'Backward Method'로 설정
plt.show()                                          #plot 시행

###Central Method###
ff3=np.zeros(98)                                    #차분 값을 저장할 ff3을 선언
for i in range(98):                                 #98회 반복
    ff3[i]=(f[i+2]-f[i])/(x[i+2]-x[i])              #ff3의 i번째에 Central Method 수행한 값 저장
plt.figure()                                        #figure 생성
plt.plot(x[:-2],ff3)                                #x축을 x[:-2], y축을 ff3으로 하여 plot
plt.xlim(-5,25)                                     #x축을 -5부터 25까지로 제한
plt.xlabel("x")                                     #x축의 이름을 'x'로 설정
plt.ylabel("y")                                     #y축의 이름을 'y'로 설정
plt.title("Central Method")                         #figure의 제목을 'Central Method'로 설정
plt.show()                                          #plot 시행

###Python Gradient Function###
ff4=np.gradient(f,x)                                #gradient 함수를 사용하여 얻은 값 ff4에 저장
plt.figure()                                        #figure 생성
plt.plot(x,ff4)                                     #x를 x축으로, ff4를 y축으로 하여 plot
plt.xlim(-5,25)                                     #x축을 -5부터 25까지로 제한
plt.xlabel("x")                                     #x축의 이름을 'x'로 설정
plt.ylabel("y")                                     #y축의 이름을 'y'로 설정
plt.title("Python Gradient")                        #figure의 제목을 'Python Gradient'로 설정
plt.show()                                          #plot 시행