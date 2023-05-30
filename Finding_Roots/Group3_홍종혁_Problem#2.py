#Problem 2

####################fixed point 구하기#################################

import numpy as np    #numpy 패키지를 np라는 이름으로 호출
from matplotlib import pyplot as plt    #matploblib 패키지의 pyplot모듈을 plt라는 이름으로 호출
x1=0.01;x2=0.01    #각 점화식의 초기값 지정
arrx=np.linspace(0,1,100)#그래프를 plot할 때 x축으로 활용할 list를 0과 1 사이를 100등분 하여 생성
value1=np.linspace(0,1,100)    #f(x)의 1행의 함수값을 저장할 리스트
value2=np.linspace(0,1,100)    #f(x)의 2행의 함수값을 저장할 리스트
arr_fx=np.array([value1,value2])    #함수 f(x)의 값을 저장할 2 by 100 배열
def func1(a, b):    #f(x)의 row 1에 있는 함수 정의
    return 0.5*a*b+0.2*(np.cos(a))

def func2(c, d):    #f(x)의 row 2에 있는 함수 정의
    return 0.3*((d)**2)-0.2*d+0.5

for i in range(len(arrx)):    #for 문을 이용하여 arrx의 길이만큼 반복
    arr_fx[0][i]=x1;arr_fx[1][i]=x2    #arr_fx의 row 1의 column i에, row 2의 column i 에 x1과 x2 값을 각각 저장
    f1 = func1(x1, x2);f2 = func2(x1, x2)    #func1, func2 함수에 x1, x2 값을 대입하여 return 값을 각각 f1, f2에 저장
    x1 = f1;x2 = f2    #f1, f2를 각각 x1, x2에 대입해 점화식 수행하게 함
plt.plot(arrx,arr_fx[0])    #arrx를 x축으로, arr_fx의 row 1을 y축으로 하는 그래프 plot
plt.plot(arrx,arr_fx[1])    #arrx를 x축으로, arr_fx의 row 2를 y축으로 하는 그래프 plot
plt.legend(['row1 convergence value','row2 convergence value'])    #각각의 선이 row1, row2의 점화식 계산 결과를 나타냄을 표시
plt.title("f(x)'s iteration graph")    #그래프의 제목 설정
plt.xlabel("x value")    #x축의 이름을 x값으로 저장
plt.ylabel("Convergence value")    #y축의 이름을 수렴값으로 저장
plt.show()    #그래프 표시 수행

##################################unique fixed point 인지 확인#####################################

def a11(a,b):    #row 1 column 1 위치의 gradient 성분을 함수로 선언
    return 0.5*b-0.2*(np.sin(a))
def a12(a):    #row 1 column 2 위치의 gradient 성분을 함수로 선언
    return 0.5*a
def a21(b):    #row 2 column 1 위치의 gradient 성분을 함수로 선언
    return 0
def a22(b):    #row 2 column 2 위치의 gradient 성분을 함수로 선언
    return 0.6*b-0.2
 
eigen=[]    #eigenvalue 계산값을 저장하기 위한 리스트 선언

for i in arrx:    #arrx내부의 성분을 모두 사용하여 for문을 통해서 반복 시행
    for j in arrx:    #arrx내부의 성분을 모두 사용하여 for문을 통해서 반복 시행
        delta = (a22(i) - a11(i,j))**2 + 4*a12(i)*a21(i)    
        #eigenvalue를 구하는 determinant 식을 세웠을 때, 근의 공식을 사용했을 때의 분자 부분의 root 내부의 식
        xo = (a11(i,j) + a22(i) + np.sqrt(delta)) / 2    #근의 공식에서 ±부분이 +인 경우
        xt = (a11(i,j) + a22(i) - np.sqrt(delta)) / 2    #근의 공식에서 ±부분이 -인 경우
        if (a11(i,j)-xo)*(a22(i)-xo) - a12(i)*a21(i) == 0:   
            eigen.append(xo)            #xo가 determinant값을 0으로 만든다면, 해당 xo값을 eigen 리스트에 저장
        if (a11(i,j)-xt)*(a22(i)-xt) - a12(i)*a21(i) == 0:    
            eigen.append(xt)            #xt가 determinant값을 0으로 만든다면, 해당 xt값을 eigen 리스트에 저장

cnt=0    #unique fixed point인지 판정하기 위한 변수 저장
for i in range(len(eigen)):    #eigen list의 길이만큼 반복문 수행
    if abs(eigen[i])>=1:cnt+=1    #eigen list의 해당 index의 절댓값이 1보다 크거나 같을 경우카운트 1 추가
if cnt>0:print('f(x) does not have unique fixed point')    
    #count값이 0보다 크면 eigenvalue의 절댓값이 1보다 작지 않은 경우가 존재한 것이므로, unique하지 않음을 출력
if cnt==0:print('f(x) has unique fixed point')    
    #count값이 0이라면 모든 eigenvalue의 절댓값이 1보다 작은 것이므로 unique fixed point임을 출력
    
##########prove by substituting#############

print(f'row1 : f1(x) - x = {arr_fx[0][-1]-x1}, row2 : f2(x) - x = {arr_fx[1][-1]-x2}')
#각 row의 함수값에서 substitution을 통해서 구한 값이 맞았음을 증명하는 식을 출력한다
print(f'fixed point for row1 : {x1}, fixed point for row2 : {x2}')    #fixed point 값을 출력
