clear       %모든 변수 초기화
clc         %명령 창 초기화
close all;  %모든 figure 닫음
load census %census 불러오기

a=[1 2 4];  %order 수를 저장한 행렬
for i=1:3   %i가 1에서 3이 될 때까지 반복하는 for문
    least_square(a(i),500*(i-1),cdate,pop);    %least_square 함수에 a(i), 500*(i-1), cdate, pop 입력
end         %for문 종료 

function least_square(n,p,cdate,pop)        %n,p,cdate,pop을 입력받는 함수를 least_square 라는 이름으로 선언
figure('Position', [p 200 560 420])         %Figure의 위치와 크기 지정
plot(cdate,pop,'o')                         %cdate를 x축, pop을 y축으로 하여 o 모양으로 plot
hold on                                     %그래프 유지
titlenum=num2str(n);                        %입력 받은 차수를 string 형태로 바꿈
title("Least Square method when order is "+titlenum)    %제목 출력
mat1=zeros(n+1,n+1);                        %mat1을 n+1 by n+1 size로 선언
mat2=zeros(n+1,1);                          %mat2를 n+1 by 1 size로 선언
for i=1:n+1                                 %i가 1에서 n+1이 될때까지 반복하는 for문 선언
    mat2(i)=sum((cdate.^(n+1-i)).*pop);     %mat2의 i번째 행에 cdate의 n+1-j제곱과 pop의 곱을 전부 합한 값을 저장
    for j=1:n+1                             %j가 1에서 n+1이 될 때까지 반복하는 for문 선언
        mat1(i,j)=sum(cdate.^(2*(n+1)-i-j));%mat1(i,j)에 cdate의 2*(n+1)-i-j제곱을 전부 합한 값을 저장
    end                                     %j를 사용한 for문 종료
end                                         %i를 사용한 for문 종료
resmat=mat1\mat2;                           %inverse(mat1)*mat2를 수행한 값을 resmat에 저장
y=0;                                        %변수 y 선ㄴ언
for k=1:n+1                                 %k가 1에서 n+1이 될 때까지 반복하는 for문 선언                           
    y=y+resmat(k)*(cdate.^(n+1-k));         %y에 resmat(k)에 cdate를 n+1-k 제곱한 것을 곱한 값을 더해줌                                  
end                                         %k를 사용한 for문 종료
plot(cdate,y,"LineWidth",1.5)               %x를 x축으로, y를 y축으로, 선 굵기를 1.5으로 plot
hold on                                     %그래프 유지
end                                         %function 마침