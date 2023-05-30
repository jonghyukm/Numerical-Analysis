#Problem 1

##################################fixed point 구하기#####################################

import numpy as np    #numpy 패키지를 np라는 이름으로 호출
from matplotlib import pyplot as plt    #matploblib 패키지의 pyplot모듈을 plt라는 이름으로 호출
x1=x2=0.01  #각 점화식의 초기값 지정
arr1=list(range(100))    #함수 1에 사용할 list 생성
arr2=list(range(100))    #함수 2에 사용할 list 생성
arrx=np.linspace(0,1,100)#그래프를 plot할 때 x축으로 활용할 list를 0과 1 사이를 100등분 하여 생성
for i in range(100):    #for 문을 이용하여 다음 사항을 100회 반복
    arr1[i] = x1;arr2[i] = x2    #arr1의 인덱스 i 지점에 x1을 지정, arr2의 인덱스 i 지점에 x2를 지정
    f1 = np.cos(np.sin(x1));f2 = np.sin(x2**(0.5))    #함수 1은 cos(sin(x)), 함수 2는 sin(x^0.5)이다. 각 함수에 x1, x2를 대입하여 변수 f1, f2에 저장
    x1 = f1;x2 = f2    #x1에 f1 값을, x2에 f2 값을 저장

def plotting(ar1,ar2,name):    #plot하기 위한 함수 생성, 각각 리스트,리스트,함수 명을 입력값으로 받을 예정임
    plt.figure()    #새로운 figure를 생성
    plt.plot(ar1,ar2)    #arrx를 x축, arr1을 y축으로 하여 그래프 그림
    plt.title(f"{name}'s iteration graph")    #그래프의 제목 설정
    plt.xlabel("x value")    #x축의 이름을 x값으로 저장
    plt.ylabel("Convergence value")    #y축의 이름을 수렴값으로 저장  
plotting(arrx,arr1,"cos(sin(x))")
plotting(arrx,arr2,"sin(√x)")
plt.show()    #plot을 그리도록 명령

##################################unique fixed point 인지 확인#####################################

np.seterr(divide='ignore')    #arrx[0]로 인해 f2_prime이 infinity로 발산하여 warning 메시지가 출력되나,
                                # 계산 수행에 문제가 없으므로 해당 메시지를 안 보이도록 설정
f1_prime=-(np.cos(arrx))*(np.sin(np.sin(arrx)))    #f1을 미분한 함수에 arrx를 대입한 값들을 f1_prime 변수에 저장
f2_prime=(1/(2*(arrx**0.5)))*(np.cos(arrx**0.5))  #f2를 미분한 함수에 arrx를 대입한 값들을 f2_prime 변수에 저장 

def check(f,fname):    #f와 fname을 받는 함수 check를 선언
    cnt=0    #unique fixed point인지 확인하게 도와주는 변수를 선언
    for i in range(len(arrx)):    #arrx의 길이만큼 for문을 이용하여 반복
        if abs(f[i])>=1:    #받아온 함수의 해당 인덱스의 절댓값이 1보다 크거나 같은 경우
            cnt+=1    #cnt 값을 1 증가 시킴
        if cnt==1:break    #만약 cnt값이 1이라면 그 즉시 해당 for 문을 중단 시킴
    if cnt==0:    #cnt값이 0이라면 해당 함수는 unique fixed point를 가지고 있음을 출력함
        print(f'{fname} has unique fixed point')
    if cnt==1:    #cnt값이 1이라면 해당 함수의 fixed point는 unique하지 않음을 출력함
        print(f'{fname} does not have unique fixed point')

check(f1_prime,"cos(sin(x))")    #f1_prime과 해당 함수명을 입력값으로 하여 check 함수 이용
check(f2_prime,"sin(√x)")    #f2_prime과 해당 함수명을 입력값으로 하여 check 함수 이용

##################################substituting solution####################################

print(f'f1(x) - x = {arr1[-1]-x1}, f2(x) - x = {arr2[-1]-x2}')    #f1에서 x1을, f2에서 x2를 빼서 솔루션이 맞았음을 증명한다.
print(f'fixed point for cos(sin(x)) : {x1}, fixed point for sin(√x) : {x2}')    #fixed point 값을 출력