function newton(N,b,x,y,point_x,open,close,y_og)        %N,b,x,y,point_x,open,close를 입력값으로 받는 함수 정의
new_mat=zeros(b);      %Netwon polynomial approximation의 수행을 위해 필요한 행렬을 b by b size로 선언
new_mat(:,1)=y(:);     %선언한 행렬의 1번째 열의 모든 행을 y값으로 채움

for k=1:1:N        %k를 1부터 1을 더해가며 N이 될 때까지 반복
    temp=zeros(1,b-k);     %값을 임시로 저장해두기 위한 행렬 1 by b-k size로 선언
    for i=k+1:1:b %i를 k+1부터 1을 더해가며 b가 될 때까지 반복
        temp(i-k)=(new_mat(i,k)-new_mat(i-1,k))/(x(i)-x(i-k));%기울기를 계산해 temp에 저장하는 작업 반복
    end     %반복문 종료
    new_mat(k+1:end,1+k)=temp(:);    %temp에 저장된 값들을 new_mat의 1+k번째 열의 k+1행부터 마지막 행까지 채움
end     %반복문 종료

new=zeros(1,N);      %Newton polynomial approxiamtion의 추정값이 담길 행렬 선언 
for j=1:1:N        %j를 1부터 1을 더해가며 N이 될 때까지 반복
    newton_x=repmat(point_x(j), 1, N)-x(1:end-1);    %행렬 x의 마지막 성분을 뺀 나머지들과 point_x의 빼기 연산을 수행(추정값을 얻기 위한 행렬임)
    for e=1:1:N    %e를 1부터 1을 더해가며 N이 될 때까지 반복
        new(j)=new(j)+new_mat(e+1,e+1)*prod(newton_x(1:e));    %대각행렬과 point_x 대입값을 곱해주는 연산 수행
    end    %반복문 종료
    new(j)=new(j)+new_mat(1,1);        %new(1,1)=y1. 즉 y1=a0를 더해주는 연산을 마무리작업으로 수행함
end     %반복문 종료

titlenum=num2str(N);    %데이터 갯수를 표시하기 위해 N을 str형으로 바꾸어 저장
figure('Position', [1000 200 540 420]);      %figure 창 띄움, [1000 200] 위치에 540x420크기로
plot(point_x,new,"LineWidth",3) %point_x를 x축으로, newton_matrix를 y축으로, 굵기 3으로 그래프를 그림
title("Netwon Polynomial Approximation when N="+titlenum)%제목 출력
xlabel("X")     %x축 이름
ylabel("Y")     %y축 이름
axis([open close min(y_og) max(y_og)]);    %축 범위 설정