#Problem4

import numpy as np    #numpy 패키지를 np라는 이름으로 호출
from matplotlib import pyplot as plt    #matploblib 패키지의 pyplot모듈을 plt라는 이름으로 호출
def f(x):    #주어진 함수를 x를 입력값으로 사용하는 함수 f로 선언
    return (x**4)+33*(x**3)+240*(x**2)-164*x-2640


########bisection method###############

def bisection(a,b):    #a,b를 입력값으로 받아 bisection method를 수행하는 함수 정의
    clist=[]    #변화하는 c값들을 저장할 list를 생성, 이는 iteration 횟수가 몇 회인지 저장하는 역할도 겸한다.
    while True:    #while문을 이용하여 무한히 반복
        c=(a+b)/2    #bisection method를 수행하기 위한 c값을 지정
        clist.append(c)    #clist list에 해당 c값을 추가
        if f(a)*f(c)<0:    #f(a)와 f(c)의 곱이 0보다 작은 경우 오른쪽 구간 끝값을 c로 변경
            b=c
        elif f(a)*f(c)>0:    #f(a)와 f(c)의 곱이 0보다 큰 경우 왼쪽 구간 끝값을 c로 변경
            a=c
        else:    #근을 구할 시, 해당 while문을 중지시킴.
            break
    return clist    #함수의 결과로 clist 반환

answer_b=[bisection(-25,-20),bisection(-13,-8),bisection(-5,0),bisection(0,5)]    #근이 있을 곳으로 추정되는 구간에서 함수를 통해 계산 수행하여 리스트에 저장

########Newton-Rhapson method###############

def ff(x2):    #f를 미분한 함수를 ff로 정의
    return 4*(x2**3)+99*(x2**2)+480*x2-164

def newton(d):    #d를 입력값으로 받아 Newton-Rhapson method를 수행하는 함수 정의
    dlist=[]    #변화하는 convergence value를 담기 위한 list 선언
    while True:    #while문을 이용하여 무한히 반복
        d=d-(f(d)/ff(d))    #Netwon method 식
        dlist.append(d)    #Netwon method dlist에 당회차의 d값 추가
        if f(d)==0:    #근을 구할 시 while문 종료
            break
    return dlist    #함수의 결과로 dlist 반환

answer_n=[newton(-25),newton(-15),newton(-5),newton(5)]    #근이 있을 곳으로 추정되는 구간에서 함수를 통해 계산 수행하여 리스트에 저장

########Secant method###############
def secant(e,g):    #e,g를 입력값으로 받아 Secant method를 수행하는 함수 정의
    elist=[]    #변화하는 convergence value값을 저장하기 위한 list 생성
    while True:    #while문을 이용하여 무한히 반복    
        e=e-(f(e)*(e-g))/(f(e)-f(g))    #Secant method 사용
        elist.append(e)    #elist에 당회차의 e값을 추가
        if f(e)==0:    #근을 구할 시 while문 종료
            break
    return elist    #함수의 결과로 elist 반환

answer_s=[secant(-25,-20),secant(-13,-8),secant(-5,0),secant(0,5)]    #근이 있을 곳으로 추정되는 구간에서 함수를 통해 계산 수행하여 리스트에 저장

#############plot function################

def method_plot(arr,name,i):    #convergence graph를 plot하기 위한 함수 선언, list 하나와 해당 방법의 이름을 입력값으로 받는다.
    x_axis = list(range(1,len(arr)+1))    #trial 횟수를 x축으로 지정
    y_axis = arr    #convergence value들이 담긴 list를 y축으로 지정
    plt.figure()    # 그래프 창 생성
    plt.title(f'Convergence plot of {name} Method {i+1}')    #어떤 방법의 plot graph인지 표기
    plt.xlabel("Number of Trials")    #x축의 이름을 시도 횟수로 저장
    plt.ylabel("Convergence value")    #y축의 이름을 수렴값으로 저장
    plt.plot(x_axis,y_axis)    #각 변수를 x축,y축으로 하여 plot
    
########plot###############

for i in range(4):    #for 문을 이용하여 각 근 별로 method들의 graph를 비교할 수 있도록 plot하고 show하는 것을 4회 반복한다.
    method_plot(answer_b[i],"Bisection",i)    #method_plot 함수를 이용하여 plot 수행
    method_plot(answer_n[i],"Newton-Rhapson",i)    #method_plot 함수를 이용하여 plot 수행
    method_plot(answer_s[i],"Secant",i)    #method_plot 함수를 이용하여 plot 수행
    plt.show()    #plot 수행    
    print(f"bisection root {i+1} : {answer_b[i][-1]}, newton rhapson root {i+1} : {answer_n[i][-1]}, secant root {i+1} : {answer_s[i][-1]}")    #각 method로 구한 답 출력