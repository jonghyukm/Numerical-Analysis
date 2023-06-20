function [x,y,point_x,b,N]=data1(N)     %N을 입력값으로 받아서 x,y,point_x,b,N을 반환하는 함수 정의
x = linspace(-5,25,N+1);    %approximation에 활용할 x성분 데이터 생성 (-5,25)구간
y = 1/sqrt(50*pi)*exp(-(x-10).^2./50);  %approximation에 활용할 y성분 데이터 생성
[a,b] = size(x);    %a,b에 각각 x 행렬의 행, 열 갯수 저장
for j=1:1:b-1   %j를 1부터 1을 더해가며 b-1가 될 때까지 반복
	point_x(1,j) = x(1,j) + (x(1,j+1) - x(1,j))/2;      %x_i와 x_i+1 들의 중간값을 저장하는 행렬 생성
end     %반복문 종료
