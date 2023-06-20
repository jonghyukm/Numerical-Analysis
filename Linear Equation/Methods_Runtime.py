###Setting up###

import numpy as np												#numpy np라는 이름으로 import	
import time														#time import					
n=int(input())													#n 입력
A = np.random.normal(0, 1, size=(n, n)) + 10000*np.identity(n)	#matrix A 설정
b = np.random.normal(0, 1, size=(n, 1))							#matrix b 설정
U=np.copy(A)													#A를 복사해 U에 저장
L=np.eye(n)														#L을 n by n 행렬로 설정
bb = np.copy(b)													#b를 복사해 bb에 저장

###LU Decomposition###
for i in range(n):						#for문 이용 n회 반복
    for j in range(i+1,n):				#for문 이용 j가 i+1에서 n-1 될 때까지 반복
        p=U[j,i]/U[i,i]					#pivot 설정
        L[j,i]=p						#L[j,i]에 pivot 기록
        U[j,:]-=p*U[i,:]				#행 연산 수행
        bb[j]-=p*bb[i]					#행 연산 수행
        
###Jacobi###
def Jacobi(A,b,xJ,prevxJ,n):						#A,b,xJ,prevxJ,n을 입력받는 함수 Jacobi 정의
    temp=np.zeros((n,1))							#temp는 n by 1 vector
    prevxJ=np.copy(xJ)								#xJ를 복사해 prevxJ에 저장
    for i in range(n):								#for문 활용 n회 반복
        temp[i]=-(A[i,:i]@xJ[:i]+A[i,i+1:]@xJ[i+1:])#Jacobi 연산 수행한 값 temp[i]에 저장
        temp[i]=(temp[i]+b[i])/A[i,i]				#Jacobi 연산 수행한 값 temp[i]에 저장
    xJ=np.copy(temp)								#xJ에 temp 복사해 저장
    return xJ,prevxJ 								#xJ, prevxJ 반환

###Gauss-Seidel###
def Gauss(A,b,xG,prevxG,n):								#A,b,xG,prevxG,n을 입력받는 함수 Gauss 정의
    temp=np.zeros((n,1))								#temp는 n by 1 vector
    prevxG=np.copy(xG)									#xG를 복사해 prevxG에 저장
    for i in range(n):									#for문 활용 n회 반복
        temp[i]=-(A[i,:i]@xG[:i]+A[i,i+1:]@prevxG[i+1:])#Gauss-Seidel 연산 수행한 값 temp[i]에 저장
        temp[i]=(temp[i]+b[i])/A[i,i]					#Gauss-Seidel 연산 수행한 값 temp[i]에 저장
        xG=np.copy(temp)								#xG에 temp 복사해 저장
    return xG,prevxG 									#xG, prevxG 반환

###Vectors###
x1=np.zeros((n,1))				#x1은 n by 1 vector
x2=np.zeros((n,1))				#x2는 n by 1 vector
xJ=np.zeros((n,1)) 				#xJ는 n by 1 vector
xG=np.zeros((n,1))				#xG는 n by 1 vector
J=np.copy(xJ)					#xJ 복사하여 J에 저장
prevJ=np.copy(xJ)				#prevJ에 xJ 복사하여 저장
G=np.copy(xG)					#G에 xG 복사하여 저장
prevG=np.copy(xG)				#prevG에 xG 복사하여 저장


###back substitution###
start_time1=time.time()							#시작 시간 저장
x1=np.zeros((n,1))							 	#x1 n by 1로 정의
x1[n-1]=bb[n-1]/U[n-1,n-1]					 	#최초의 back substitution 수행
for i in range(n):						     	#for문 이용 n회 반복
    k=n-1-i									 	#k에 n-1-i 저장
    x1[k]=(bb[k]-U[k,k+1:n]@x1[k+1:n])/U[k,k]	#x1[k]에 해당 연산 수행한 값 저장
print(f"Back substitution took {(time.time() - start_time1)*(10)**3} ms for computing")
												#소요 시간 출력

###LU Decomposition###
start_time2=time.time()					#시작 시간 저장
invL=np.linalg.inv(L)					#invL에 L의 inverse matrix 저장
invU=np.linalg.inv(U)					#invU에 U의 inverse matrix 저장
y=invL@b								#y=L^-1b 연산 수행
x2=invU@y								#x2=U^-1y 연산 수행
print(f"LU Decomposition Algorithm took {(time.time() - start_time2)*(10)**3} ms for computing")
										#소요 시간 출력
###Jacobi###
start_time3=time.time()					#시작 시간 저장
while True:								#while문 무한 반복
    J,prevJ=Jacobi(A,b,J,prevJ,n)		#A,b,xJ,prevxJ,n을 입력받아 반환값을 J,prevJ에 저장
    if np.allclose(J,prevJ,1e-100):		#J와 prevJ의 오차 범위가 10^-100 이내라면
        xJ=J							#J를 xJ에 저장
        break							#while문 종료
print(f"Jacobi Algorithm took {(time.time() - start_time3)*(10)**3} ms for computing")
										#소요 시간 출력
###Gauss-Seidel###	
start_time4=time.time()					#시작 시간 저장
while True:								#while문 무한 반복
    G,prevG=Gauss(A,b,G,prevG,n)		#A,b,xG,prevxG,n을 입력받아 반환값을 G,prevG에 저장
    if np.allclose(G,prevG,1e-100):		#G와 prevG의 오차 범위가 10^-100 이내라면
        xG=G							#G를 xG에 저장
        break							#while문 종료
print(f"Gauss-Sediel Algorithm took {(time.time() - start_time4)*(10)**3} ms for computing")
										#소요 시간 출력
###Numpy###
start_time5=time.time()					#시작 시간 저장
solve=np.linalg.solve(A,b)				#선형방정식의 solution 저장
print(f"numpy.linalg.solve took {(time.time() - start_time5)*(10)**3} ms for computing")
										#소요 시간 출력
###Check Accuracy###
def accuracy(x,solution):					#x, solution을 입력 받는 함수 선언
    i=1										#변수 i 선언	
    while True:								#while문 무한 반복
        error=10**(-i)						#error는 10^(-i)
        if np.array_equal(x,solution):	  	#x와 solution이 같다면 i=-1 저장하고 while문 종료
            i=-1
            break
        if np.allclose(x,solution,error): 	#x와 solution이 오차범위 error 내에서 근사하면 i에 1 더함
            i+=1
        else:								#범위 내에서 근사하지 않는다면 while문 종료
            break
        if i>=10000:						#i가 10000보다 크거나 같으면 while문 종료
            break
    return i   								#i 반환
acc1=accuracy(x1,solve)										#acc1에 x1,solve로 함수 수행한 값 저장
acc2=accuracy(x2,solve)										#acc2에 x2,solve로 함수 수행한 값 저장
accJ=accuracy(xJ,solve)										#accJ에 xJ,solve로 함수 수행한 값 저장
accG=accuracy(xG,solve)										#accG에 xG,solve로 함수 수행한 값 저장
print(f"Back substitution's Accuracy point is {acc1}")		#해당 method의 Accuracy point 값 출력
print(f"LU Decomposition's Accuracy point is {acc2}")		#해당 method의 Accuracy point 값 출력
print(f"Jacobi Algorithm's Accuracy point is {accJ}")		#해당 method의 Accuracy point 값 출력	
print(f"Gauss-Sediel Algorithm's Accuracy point is {accG}")	#해당 method의 Accuracy point 값 출력
