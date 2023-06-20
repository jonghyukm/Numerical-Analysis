###Setting up###
import numpy as np						                        #numpy np라는 이름으로 import						
n=int(input())							                        #n 입력
A = np.random.normal(0, 1, size=(n, n)) + 10000*np.identity(n)  #matrix A 설정
b = np.random.normal(0, 1, size=(n, 1))	                        #matrix b 설정
U=np.copy(A)							                        #A를 복사해 U에 저장
L=np.eye(n)								                        #L을 n by n 행렬로 설정
P=np.eye(n)                                                     #P를 n by n 행렬로 설정
bb = np.copy(b)							                        #b를 복사해 bb에 저장

###row_exchange###                                              
def row_exchange(A,B,C,i,j):            #행 교환 수행하는 함수 선언                     
    temp1 = np.copy(A[i, :])            #temp1에 교환할 행 저장
    A[i, :] = np.copy(A[j, :])          #교환 시행
    A[j, :] = np.copy(temp1)            #교환 시행
    temp2 = np.copy(B[i, :])            #temp2에 교환할 행 저장
    B[i, :] = np.copy(B[j, :])          #교환 시행
    B[j, :] = np.copy(temp2)            #교환 시행
    temp3 = np.copy(C[i, :])            #temp3에 교환할 행 저장
    C[i, :] = np.copy(C[j, :])          #교환 시행
    C[j, :] = np.copy(temp3)            #교환 시행
    return A,B,C                        #A,B,C 반환

###PA=LU decomposition###
for i in range(n):                      #for문 이용 n회 반복
    if U[i,i]==0:                       #pivot이 0인 경우
        k=np.argmax(abs(U[i:n,i]))+i    #abs(U[i:n,i])의 max 값 index를 k에 저장
        U,P,bb=row_exchange(U,P,bb,i,k) #row exchange 수행
    for j in range(i+1,n):              #for문 이용 j가 i+1에서 n-1 될 때까지 반복
        L[j, i]=U[j, i]/U[i, i]         #L[j,i]에 pivot 기록
        U[j, :]-=L[j, i]*U[i, :]        #행 연산 수행
        bb[j]-=L[j, i]*bb[i]            #행 연산 수행
        
###Check the uniquness of the solution###
rank=np.linalg.matrix_rank(A)			#rank에 A의 rank 저장
det=np.linalg.det(A)					#det에 A의 determinant 저장
eig,eigv=np.linalg.eig(A)				#eig,eigv에 A의 eigenvalue,eigenvector 저장
if rank!=n:print("not unique")			#rank가 n이 아니면 not unique 출력
else:print("Unique, By rank")			#n이면 Unique,By rank 출력
if det==0:print("not unique")			#det가 0이면 not unique 출력
else:print("Unique, By determinant")	#0이 아니면 Unique,By determinant 출력
if 0 in eig:print("not unique")			#eig에 0이 있으면 not unique출력
else:print("Unique, By eigenvalue")		#아니라면 Unique,By eigenvalue출력

###Back substitution###
x1=np.zeros((n,1))							    #x1 n by 1로 정의
x1[n-1]=bb[n-1]/U[n-1,n-1]					    #최초의 back substitution 수행
for i in range(n):						        #for문 이용 n회 반복
    k=n-1-i									    #k에 n-1-i 저장
    x1[k]=(bb[k]-U[k,k+1:n]@x1[k+1:n])/U[k,k]   #x1[k]에 해당 연산 수행한 값 저장 
    
###Solution By LU Decomposition###
invL=np.linalg.inv(L)					#invL에 L의 inverse matrix 저장
invU=np.linalg.inv(U)					#invU에 U의 inverse matrix 저장
invP=np.linalg.inv(P)                   #invP에 P의 inverse matrix 저장
pb=P@b                                  #pb에 P와 b의 곱 저장
y=invL@pb								#y=L^-1b 연산 수행
x2=invU@y								#x2=U^-1y 연산 수행

###Verify###
solve=np.linalg.solve(A,b)				#solve에 선형방정식 solution 저장
if np.allclose(x1,solve,1e-9):			#오차 값이 10^-9 이내면 해당 메시지 출력
    print(f"Back substitution converges to the solution in very small error : 10^-9")
if np.array_equal(x1,solve):			#두 array 동일할 시 해당 메시지 출력		
    print(f"Back substitution matched perfectly to the solution")
if np.allclose(x2,solve,1e-9):          #오차 값이 10^-9 이내면 해당 메시지 출력
    print(f"LU Decomposition converges to the solution in very small error : 10^-9")
if np.array_equal(x2,solve):			#두 array 동일할 시 해당 메시지 출력
    print(f"LU Decomposition matched perfectly to the solution")
if np.allclose(P@A,L@U,1e-9):           #오차 값이 10^-9 이내면 해당 메시지 출력
    print(f"PA and LU converges in very small error : 10^-9")
if np.array_equal(P@A,L@U):             #두 array 동일할 시 해당 메시지 출력
    print(f"PA and LU  matched perfectly")