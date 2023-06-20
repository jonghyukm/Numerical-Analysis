close all;  %열려 있는 plot 창 모두 닫기
clear   %모든 변수 초기화
clc     %명령 창 초기화

%% Plot original function
x_og = linspace(0,10,100);   %original function의 x축 성분 생성 (0,10)구간
y_og = 2*exp(-x_og) + (exp(-0.1*x_og).*sin(((pi/2)*x_og)+pi/4));   %original function의 y축 성분 생성
figure('Position', [0 200 540 420]);     %figure 생성, [0,200]위치에 540x420크기로 
plot(x_og,y_og,"LineWidth",3)    %x_original과 y_original을 각각 x축, y축으로 하여, 3의 굵기로 그래프 그림
title("Original function")      %제목 설정
xlabel("X")     %x축 이름 설정
ylabel("Y")     %y축 이름 설정
axis([0 10 min(y_og) max(y_og)]);       %축 범위 설정

%% Plot Approximation
for iter=1:3        %iter가 1에서 3이 될 때까지 반복 
    datanum = [40 10 3];    %approximation을 수행하기 위해 생성할 데이터의 개수 저장
    [x,y,point_x,b,N]=data2(datanum(iter));    %데이터 생성
    lagrange(N,b,x,y,point_x,0,10,y_og)   %lagrange approximation 수행
    newton(N,b,x,y,point_x,0,10,y_og)     %Newton polynomial approximation 수행
end      %반복문 종료