clear       %모든 변수 초기화
clc         %명령 창 초기화
close all;  %모든 figure 닫음
load census %census 불러오기

spline_first(cdate,pop)     %spline_first 함수 실행
spline_second(cdate,pop)    %spline_second 함수 실행

function spline_first(cdate,pop)        %spline_first 함수 선언
figure('Position', [200 200 560 420])   %figure 생성 관련 세팅
plot(cdate,pop,'o')                     %원본 데이터 plot        
title("First Order Spline Fit")         %제목 설정
hold on                                 %그래프 유지 
temp_y=zeros(1,length(cdate)-1);        %y값을 담아둘 행렬 생성
m=zeros(1,length(cdate));               %기울기 값을 저장할 행렬 생성
for j=1:length(cdate)-1                 %j가 1에서 length(cdate)-1이 될때까지 반복
    m(j)=((pop(j+1)-(pop(j)))/((cdate(j+1))-(cdate(j)))); %pop변화값을 cdate 변화값으로 나눈 값을 m의 j 열에 저장
    x=linspace(cdate(j),cdate(j+1),length(cdate)-1);    %cdate(j)와 cdate(j+1)사이를 length(cdate)-1등분 한 x 선언  
    for k=1:length(cdate)-1     %k가 1에서 length(cdate)-1이 될때까지 반복
        temp_y(k)=m(j)*(x(k)-cdate(j))+pop(j);  %temp_y의 k번째 열에 해당하는 범위에 spline을 시행한 값을 저장
    end                                 %반복문 종료
    plot(x,temp_y,"LineWidth",1.5)      %해당 그래프 plot
    hold on                             %그래프 유지
end                                     %for문 종료
end                                     %함수 닫음

function spline_second(cdate,pop)       %spline_second 함수 선언
figure('Position', [800 200 560 420])   %figure 생성, 위치 지정
plot(cdate,pop,'o')                     %원본 데이터 plot        
title("Second Order Spline Fit")         %제목 설정
hold on                                 %그래프 유지 
a=zeros((length(cdate)-1)*3);           %(length(cdate)-1)*3 by (length(cdate)-1)*3 size 행렬 선언 
b=zeros((length(cdate)-1)*3,1);         %(length(cdate)-1)*3 by 1 size 행렬 선언

%% f(x)값 처리
for i=1:2:(length(cdate)-1)*2-1             %i가 1에서 (length(cdate)-1)*2-1이 될때까지 2씩 더하며 반복
    k=(3*(i-1))/2;                          %k 값 선언
    for j=1:3                               %j가 1에서 3 될때까지 반복   
        a(i,k+j)=(cdate((i+1)/2))^(3-j);    %a 행렬의 i행의 k+j열에 cdate((i+1)/2)의 (3-j)제곱을 저장
        a(i+1,k+j)=(cdate((i+3)/2))^(3-j);  %a 행렬의 i+1행의 k+j열에 cdate((i+3)/2)의 (3-j)제곱을 저장
    end                                     %for문 종료
    b(i)=pop((i+1)/2);                      %b 행렬의 i번째 행에 pop((i+1)/2)저장
    b(i+1)=pop((i+3)/2);                    %b 행렬의 i+1번째 행에 pop((i+3)/2) 저장    
end                                         %for문 종료

%% f'(x)값 처리 - smoothing
for i=1:length(cdate)-2                     %i가 1에서 legnth(cdate)-2가 될때까지 반복
    k=3*(i-1);                              %k에 3*(i-1)값 저장
    for j=1:3                               %j가 1에서 3이 될때까지 반복
        if j==1                                             %j가 1이라면
            a(i+(length(cdate)-1)*2,k+j)=2*cdate(i+1);      %a(i+(length(cdate)-1)*2,k+j)에 2*cdate(i+1)저장
            a(i+(length(cdate)-1)*2,3+j+k)=-2*cdate(i+1);   %a(i+(length(cdate)-1)*2,3+k+j)에 -2*cdate(i+1)저장
        elseif j==2                                         %j가 2라면
           a(i+(length(cdate)-1)*2,j+k)=1;                  %a(i+(length(cdate)-1)*2,k+j)에 1저장
           a(i+(length(cdate)-1)*2,3+j+k)=-1;               %a(i+(length(cdate)-1)*2,3+k+j)에 -1저장
        elseif j==3                                         %j가 3이라면    
            a(i+(length(cdate)-1)*2,j+k)=0;                 %a(i+(length(cdate)-1)*2,k+j)에 0저장
            a(i+(length(cdate)-1)*2,3+j+k)=0;               %a(i+(length(cdate)-1)*2,3+k+j)에 0저장
        end                                                 %if문 종료 
    end                                                     %for문 종료
end                                                         %for문 종료

%% f''(x)값 처리
a(end,1)=1;     %a(end,1)=1에 1 저장
c=a\b;          %c에 inv(a)*b 저장

for j=1:3:length(c)                                             %j가 1에서 length(c)가 될때까지 3씩 더해가며 반
    y=zeros(1,length(cdate)-1);                                 %y값 저장할 행렬 선언
    x=linspace(cdate((j+2)/3),cdate((j+5)/3),length(cdate)-1);  %x는 구간 cdate((j+2)/3),cdate((j+5)/3)를 length(cdate)-1등분한 행렬
    for k=1:length(cdate)-1                                     %k가 1에서 length(cdate)-1이 될때까지 반복
        y(k)=c(j)*(x(k)^2)+c(j+1)*x(k)+c(j+2);                  %y(k)에 c(j)*(x(k)^2)+c(j+1)*x(k)+c(j+2)라는 2차식 저장
    end                                                         %for문 종료
    plot(x,y,"LineWidth",1.5)                                   %approximation graph plot
    hold on                                                     %그래프 유지
end                                                             %for문 종료
end            %함수 닫음