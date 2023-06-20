function lagrange(N,b,x,y,point_x,open,close,y_og)      %N,b,x,y,point_x,open,close를 입력값으로 받는 함수 정의
lag = zeros(1, N);     %Lagrange approxiamtion의 추정값이 담길 행렬 선언 

for i = 1:1:N      %i를 1부터 1을 더해가며 N이 될 때까지 반복
    for k = 1:1:b      %k를 1부터 1을 더해가며 b가 될 때까지 반복
        lag_x = [x(1:k-1) x(k+1:end)];       %lagrange approximation을 수행하기 위해, 행렬 x에서 k번째 성분을 뺀 행렬 저장 
        num = point_x(i) - lag_x;       %lagrange approximation의 각 항들의 분자 부분에 들어갈 성분 저장
        den = x(k) - lag_x;           %lagrange approximation의 각 항들의 분모 부분에 들어갈 성분 저장
        lag(i)=lag(i)+y(k)*(prod(num(:))/prod(den(:)));%분수 연산을 마친 후 k번째 y성분을 곱해주어 행렬에 저장
    end     %반복문 종료
end         %반복문 종료

titlenum=num2str(N);    %데이터 갯수를 표시하기 위해 N을 str형으로 바꾸어 저장
figure('Position', [500 200 540 420]); %figure 창 띄움, [500 200] 위치에 540x420크기로
plot(point_x, lag,"LineWidth",3) %point_x를 x축으로, lag를 y축으로, 굵기 3으로 그래프를 그림
title("Lagrange Approximation when N="+titlenum)    %제목 출력
xlabel("X")     %x축 이름
ylabel("Y")     %y축 이름
axis([open close min(y_og) max(y_og)]);