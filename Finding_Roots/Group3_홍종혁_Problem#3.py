# Problem3

#####given function's graph#######

import numpy as np  # numpy 패키지를 np라는 이름으로 호출
from matplotlib import pyplot as plt  # matploblib 패키지의 pyplot모듈을 plt라는 이름으로 호출
def f(x):  # 주어진 함수를 x를 입력값으로 사용하는 함수 f로 선언
    return np.exp(-0.5 * x) * (4 - x) - 2
arrx = np.linspace(0, 10, 100)  # 그래프를 plot할 때 x축으로 활용할 list를 0과 10 사이를 100등분 하여 생성
plt.title("Graph of given Function")  # 그래프의 제목 설정
plt.xlabel("X-axis")  # x축의 이름을 "X-axis"로 저장
plt.ylabel("Y-axis")  # y축의 이름을 "Y-axis"로 저장
plt.plot(arrx, f(arrx))  # arrx를 x축으로, 입력값으로 arrx를 받은 함수 f를 y축으로 하여 plot
plt.show()    #그래프 표시 수행

########bisection method###############

a = 0.0  # 왼쪽 구간 끝 값 설정
b = 10.0  # 오른쪽 구간 끝 값 설정
clist = []  # 변화하는 c값들을 저장할 list를 생성, 이는 iteration 횟수가 몇 회인지 저장하는 역할도 겸한다.
while True:  # while문을 이용하여 무한히 반복
    c = (a + b) / 2  # bisection method를 수행하기 위한 c값을 지정
    clist.append(c)  # clist list에 해당 c값을 추가
    if f(a) * f(c) < 0:  # f(a)와 f(c)의 곱이 0보다 작은 경우 오른쪽 구간 끝값을 c로 변경
        b = c
    elif f(a) * f(c) > 0:  # f(a)와 f(c)의 곱이 0보다 큰 경우 왼쪽 구간 끝값을 c로 변경
        a = c
    else:  # 근을 구할 시, 해당 while문을 중지시킴.
        break
print(f"Bisection method's answer: {c}")    #해당 method로 구한 정답 출력

########Newton-Rhapson method###############

def ff(x2):  # f를 미분한 함수를 ff로 정의
    return (np.exp(-0.5 * x2) * (x2 - 6)) / 2

d = 0  # 초기값을 0으로 설정
dlist = [d]  # 변화하는 convergence value를 담기 위한 list 선언
while True:  # while문을 이용하여 무한히 반복
    d = d - (f(d) / ff(d))  # Netwon method 식
    dlist.append(d)  # Netwon method dlist에 당회차의 d값 추가
    if f(d) == 0:  # 근을 구할 시 while문 종료
        break
print(f"Newton-Rhapson method's answer: {d}")    #해당 method로 구한 정답 출력

########Secant method###############

e = 0;g = 1  # 구간 설정
elist = [0]  # 변화하는 convergence value값을 저장하기 위한 list 생성
while True:  # while문을 이용하여 무한히 반복
    e = e - (f(e) * (e - g)) / (f(e) - f(g))  # Secant method 사용
    elist.append(e)  # elist에 당회차의 e값을 추가
    if f(e) == 0:  # 근을 구할 시 while문 종료
        break 
print(f"Secant method's answer: {e}")    #해당 method로 구한 정답 출력

#################plot function###########

def method_plot(arr, name):  # convergence graph를 plot하기 위한 함수 선언, list 하나와 해당 방법의 이름을 입력값으로 받는다.
    x_axis = list(range(1, len(arr) + 1))  # trial 횟수를 x축으로 지정
    y_axis = arr  # convergence value들이 담긴 list를 y축으로 지정
    plt.figure()  # 그래프 창 생성
    plt.title(f'Convergence plot of {name} Method')  # 어떤 방법의 plot graph인지 표기
    plt.xlabel("Number of Trials")  # x축의 이름을 시도 횟수로 저장
    plt.ylabel("Convergence value")  # y축의 이름을 수렴값으로 저장
    plt.plot(x_axis, y_axis)  # 각 변수를 x축,y축으로 하여 plot

########method plot###############
method_plot(clist, "Bisection")  # Bisection method에 대한 plot 수행
method_plot(dlist, "Newton-Rhapson")  # Newton-Rhapson method에 대한 plot 수행
method_plot(elist, "Secant")  # Secant method에 대한 plot 수행
plt.show()    #그래프 표시 수행
