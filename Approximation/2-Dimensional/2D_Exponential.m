clear       %모든 변수 초기화
clc         %명령 창 초기화
close all;  %모든 figure 닫음
load census %census 불러오기
plot(cdate,pop,'o')          %cdate를 x축, pop을 y축으로 하여 o 모양으로 plot
hold on    %그래프 유지
title("Exponential Fit")    %제목 작성
log_pop=log(pop);    %log를 취한 pop을 log_pop에 저장
exponential(cdate,log_pop)  %exponential 함수에 cdate,log_pop을 입력

function exponential(cdate,pop) %두 가지 입력값을 받는 함수 exponential을 선언
mat1=zeros(2,2);    %2 by 2 size의 matrix 생성
mat2=zeros(2,1);    %2 by 1 size의 matrix 생성
for i=1:2           %i가 1에서 2가 될 때까지 반복
    mat2(i)=sum((cdate.^(2-i)).*pop);   %mat2의 i번째 행에 cdate의 2-i제곱과 pop을 곱한 값의 합을 저장
    for j=1:1:2     %j가 1에서 2가 될 때까지 반복
        mat1(i,j)=sum(cdate.^(4-i-j));  %mat1의 i번째 행 j번째 열에 cdate의 4-i-j 제곱의 합을 저장
    end             %반복문 종료
end                 %반복문 종료
resmat=mat1\mat2;   %inv(mat1)*mat2를 resmat에 저장
resmat(2)=exp(resmat(2));               %resmat(2)를 exp에 대입해 C를 찾아줌
y=resmat(2).*exp(cdate.*resmat(1));     %resmat(2)와 exp(cdate와 resmat(1)을 곱한 값)을 곱한값을 y에 저장 
plot(cdate,y,"LineWidth",1.5)           %cdate를 x축, y를 y축으로 하여 plot
end                 %함수 닫음