###Setting up###
import numpy as np						                        #numpy np라는 이름으로 import
from matplotlib import pyplot as plt                            #pyplot plt라는 이름으로 import						
n=int(input())							                        #n 입력
A = np.random.normal(0, 1, size=(n, n)) + 10000*np.identity(n)  #matrix A 설정
b = np.random.normal(0, 1, size=(n, 1))	                        #matrix b 설정
solve=np.linalg.solve(A,b)				                        #선형방정식 solution solve에 저장

###Jacobi###
def Jacobi(A,b,xJ,prevxJ,n):						#A,b,xJ,prevxJ,n을 입력받는 함수 Jacobi 정의
    temp=np.zeros((n,1))							#temp는 n by 1 vector
    prevxJ=np.copy(xJ)								#xJ를 복사해 prevxJ에 저장
    for i in range(n):								#for문 활용 n회 반복
        temp[i]=-(A[i,:i]@xJ[:i]+A[i,i+1:]@xJ[i+1:])#Jacobi 연산 수행한 값 temp[i]에 저장
        temp[i]=(temp[i]+b[i])/A[i,i]				#Jacobi 연산 수행한 값 temp[i]에 저장
    xJ=np.copy(temp)								#xJ에 temp 복사해 저장
    return xJ,prevxJ 								#xJ, prevxJ 반환
xJ=np.zeros((n,1))						#xJ는 n by 1 vector
cntJ=0  								#변수 cntJ 선언
cntJ_index=[0]							#변화하는 cntJ 값 저장할 리스트 cntJ_index 선언
J=np.copy(xJ)							#J는 n by 1 vector
prevJ=np.copy(xJ)						#prevJ는 n by 1 vector
estJ=np.zeros((n,1))					#estJ는 n by 1 vector
while True:								#while문 무한 반복
    cntJ+=1								#cntJ 1 증가
    cntJ_index.append(cntJ)				#cntJ 값을 cntJ_index에 추가
    J,prevJ=Jacobi(A,b,J,prevJ,n)		#A,b,xJ,prevxJ,n을 입력받아 반환값을 J,prevJ에 저장
    if np.allclose(J,prevJ,1e-100):		#J와 prevJ의 오차 범위가 10^-100 이내라면
        xJ=J							#J를 xJ에 저장
        break							#while문 종료
    estJ=np.hstack((estJ, J))			#estJ에 J 이어붙임
estJ=np.hstack((estJ, xJ))				#estJ에 J 이어붙임

###Gauss-Seidel###
def Gauss(A,b,xG,prevxG,n):								#A,b,xG,prevxG,n을 입력받는 함수 Gauss 정의
    temp=np.zeros((n,1))								#temp는 n by 1 vector
    prevxG=np.copy(xG)									#xG를 복사해 prevxG에 저장
    for i in range(n):									#for문 활용 n회 반복
        temp[i]=-(A[i,:i]@xG[:i]+A[i,i+1:]@prevxG[i+1:])#Gauss-Seidel 연산 수행한 값 temp[i]에 저장
        temp[i]=(temp[i]+b[i])/A[i,i]					#Gauss-Seidel 연산 수행한 값 temp[i]에 저장
        xG=np.copy(temp)								#xG에 temp 복사해 저장
    return xG,prevxG 									#xG, prevxG 반환
xG=np.zeros((n,1))						#xG는 n by 1 vector
cntG=0  								#변수 cntG 선언
cntG_index=[0]							#변화하는 cntG 값 저장할 리스트 cntG_index 선언
G=np.copy(xG)							#G는 n by 1 vector
prevG=np.copy(xG)						#prevG는 n by 1 vector
estG=np.zeros((n,1))					#estG는 n by 1 vector
while True:								#while문 무한 반복
    cntG+=1								#cntG 1 증가
    cntG_index.append(cntG)				#cntG 값을 cntG_index에 추가
    G,prevG=Gauss(A,b,G,prevG,n)		#A,b,xG,prevxG,n을 입력받아 반환값을 G,prevG에 저장
    if np.allclose(G,prevG,1e-100):		#G와 prevG의 오차 범위가 10^-100 이내라면
        xG=G							#G를 xG에 저장
        break							#while문 종료
    estG=np.hstack((estG, G))			#estG에 G 이어붙임
estG=np.hstack((estG, xG))				#estG에 G 이어붙임

###Plot the Jacobi Convergence###
plt.figure								#figure 생성
for i in range(n):    					#for문 활용 n회 반복
    plt.plot(cntJ_index,estJ[i,:])		#cntJ_index,estJ 사용하여 plot
plt.title("Jacobi Convergence")			#제목 설정
plt.xticks(np.arange(0, cntJ+1))		#x축 눈금 설정
plt.show()								#plot 수행

###Plot the Gauss-Seidel Convergence###
plt.figure								#figure 생성
for i in range(n):    					#for문 활용 n회 반복
    plt.plot(cntG_index,estG[i,:])		#cntG_index,estG 사용하여 plot
plt.title("Gauss-Seidel Convergence")			#제목 설정
plt.xticks(np.arange(0, cntG+1))		#x축 눈금 설정
plt.show()								#plot 수행

###Plot square error for Jacobi###
estSEJ=(solve-estJ[:,0].reshape(-1,1))**2							#estSEJ의 초기값 설정
for i in range(1,len(estJ[0,:])):									#for문 사용하여 반복
    estSEJ=np.hstack((estSEJ,(solve-estJ[:,i].reshape(-1,1))**2))	#estSEJ에 square error 저장
plt.figure										#figure 생성
for i in range(n):    							#for문 활용 반복
    plt.plot(cntJ_index,estSEJ[i,:])			#cntJ_index, estSEJ 사용하여 plot
plt.title("Jacobi square error Convergence")	#제목 설정
plt.xticks(np.arange(0, cntJ+1))				#x축 눈금 설정
plt.show()										#plot 수행

###Plot square error for Gauss-Seidel###
estSEG=(solve-estG[:,0].reshape(-1,1))**2							#estSEG의 초기값 설정
for i in range(1,len(estG[0,:])):									#for문 사용하여 반복
    estSEG=np.hstack((estSEG,(solve-estG[:,i].reshape(-1,1))**2))	#estSEG에 square error 저장
plt.figure										#figure 생성
for i in range(n):    							#for문 활용 반복
    plt.plot(cntG_index,estSEG[i,:])			#cntG_index, estSEG 사용하여 plot
plt.title("Gauss-Seidel square error Convergence")	#제목 설정
plt.xticks(np.arange(0, cntG+1))				#x축 눈금 설정
plt.show()										#plot 수행
