clear       %변수 초기화
clc         %명령창 초기화    
load census_3d.mat      %census_3d 불러오기
close all;  %모든 figure 닫음

a=[1 2];    %order 수를 저장한 행렬
for i=1:2   %i가 1에서 2가 될 때까지 반복하는 for문
    least_square3D(a(i),800*(i-1)+100,census_3D)
    %least_square3D 함수에 a(i), 800*(i-1)+100, census_3D 입력
end         %for문 종료 


%% 함수

function least_square3D(n,p,census_3D) 
%n,p,census_3D를 입력받는 함수를 least_square3D 라는 이름으로 선언
cx1=census_3D(:,1);     %census_3d의 첫번째 열을 cx1에 저장
cx2=census_3D(:,2);     %census_3d의 두번째 열을 cx2에 저장
cy=census_3D(:,3);      %census_3d의 세번째 열을 y에 저장
figure('Position', [p 200 560 420])  %figure 위치와 크기 지정
plot3(cx1,cx2,cy,"o")   %cx1,cx2를 x1,x2축으로, cy를 y축으로 하여 o 모양으로 plot
hold on                 %그래프 유지
titlenum=num2str(n);    %입력 받은 차수를 string 형태로 바꿈
title("Least Square method when order is "+titlenum)    %제목 출력
mat1=zeros(2*n+1,2*n+1);    %mat1을 2n+1 by 2n+1 size로 선언
mat2=zeros(2*n+1,1);        %mat2를 2n+1 by 1 size로 선언
k=n+1;                      %경계값 k를 n+1로 선언
for i=1:2*n+1               %i가 1에서 2n+1이 될때까지 반복하는 for문 선언
    if i<=k                 %i가 k보다 작거나 같을 때
        mat2(i)=sum((cx1.^(i-1)).*cy);  %mat2(i)에 (cx1.^(i-1)).*cy의 합 저장
        for j=1:2*n+1       %j가 1에서 2n+1이 될 때까지 반복하는 for문 선언
            if j<=k         %j가 k보다 작거나 같을 때
                mat1(j,i)=sum(cx1.^(i+j-2));    %mat1(j,i)에 cx1.^(i+j-2)의 합 저장
            else            %j가 k보다 크면
                mat1(j,i)=sum((cx2.^(j-k)).*(cx1.^(i-1))); %mat1(j,i)에 (cx2.^(j-k)).*(cx1.^(i-1))의 합 저장
            end             %if문 종료
        end                 %for문 종료
    else                    %i가 k보다 크면
        mat2(i)=sum((cx2.^(i-k)).*cy);      %mat2(j,i)에 (cx2.^(i-k)).*cy의 합 저장
        for j=1:2*n+1       %j가 1에서 2n+1이 될때까지 반복하는 for문 선언
            if j<=k         %j가 k보다 작거나 같으면
                mat1(j,i)=sum((cx1.^(j-1)).*(cx2.^(i-k)));  %mat1(j,i)에 (cx1.^(j-1)).*(cx2.^(i-k))합 저장
            else            %j가 k보다 크면 
                mat1(j,i)=sum(cx2.^(i+j-2*k));  %mat1(j,i)에 cx2.^(i+j-2*k) 합 저장
            end             %if문 종료
        end                 %for문 종료
    end                     %if문 종료
end                         %for문 종료
resmat=mat1\mat2;           %resmat에 inv(mat1)*mat2 값 저장
y=0;                        %변수 y 선언
for i=1:2*n+1               %i가 1에서 2n+1이 될 때까지
    if i<=k                 %i가 k보다 작거나 같으면
        y=y+resmat(i)*(cx1.^(i-1));     %y에 resmat(i)와 cx1.^(i-1)곱한 값 저장
    else                    %i가 k보다 크면
        y=y+resmat(i)*(cx2.^(i-k));     %y에 resmat(i)와 cx2.^(i-k)곱한 값 저장
    end                     %if문 종료
end                         %for문 종료
plot3(cx1,cx2,y,"LineWidth",1.5)        %Approximation 결과 plot
end                         %함수 닫음


