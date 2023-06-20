import numpy as np                                          #numpy를 np라는 이름으로 호출
import scipy as sp                                          #scipy를 sp라는 이름으로 호출
x=np.linspace(-200,200,401)                                 #linspace를 사용하여 -200,200사이에서 401개의 point x에 저장
def f(x):                                                   #x를 입력 받는 함수 f 정의
    return (1/np.sqrt(50*(np.pi)))*(np.exp((-(x-10)**2)/50))#주어진 수식에 x 대입한 값 return
g=f(x)                                                      #g에 f(x)값 저장

###Trapezoidal Method###                
I1=0                                                        #변수 I1 선언                                                        
for i in range(len(x)-1):                                   #len(x)-1 만큼 반복
    I1+=((x[i+1]-x[i])*(g[i+1]+g[i]))/2                     #I1에 Trapezoidal Method 수행한 값 저장
print(f'Trapezoidal Method : {I1}')                         #Trapezoidal Method를 통해 얻은 적분 값 출력

###Simpson's Method###
I2=0                                                        #변수 I2 선언
x2=np.linspace(-200,200,801)                                #linspace를 사용하여 -200,200사이에서 801개의 point를 x2에 저장
tempg=(1/np.sqrt(50*(np.pi)))*(np.exp((-(x2-10)**2)/50))    #tempg 변수에 주어진 수식에 x2를 대입한 값 저장
for i in range(len(x)-1):                                   #len(x)-1 만큼 반복
    I2+=((x[i+1]-x[i])/6)*(g[i]+4*tempg[2*i+1]+g[i+1])      #I2에 Simpson's Rule 수행한 값 저장
print(f"Simpson's Method : {I2}")                           #Simpson's Method를 통해 얻은 적분 값 출력

###Euler's Method###
I3=0                                                        #변수 I3 선언
for i in range(len(x)-1):                                   #len(x)-1만큼 반복
    I3+=g[i]*(x[i+1]-x[i])                                  #I3에 Euler's Method 수행한 값 저장
print(f"Euler's Method : {I3}")                             #Euler's Method를 통해 얻은 적분 값 출력

###Python Numerical Integration Method###               
I4,I4E=sp.integrate.quad(f,-200,200)                        #변수 I4,I4E에 각각 적분 값, 오차 저장
print(f"Python Numerical Integration Method : {I4}")        #Python의 Numerical Integration Method를 통해 얻은 적분 값 출력