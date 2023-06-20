function C=Fourier(x,t,N,T,dx)                          %Fourier 변환 함수 정의
w=2*pi/T;                                               %각주파수값 설정
C=zeros(1,2*N+1);                                       %Fourier coefficient 값 초기화
dt=t(2)-t(1);                                           %시간 간격 저장
for m=1:2*N+1                                           %2*N+1회 반복
    temp=0;                                             %temp 값 초기화
    for n=1:T*(1/dx)+1                                  %T*(1/dx)+1회 반복
        temp=temp+x(n)*exp(-1i*t(n)*w*(m-(N+1)))*dt;    %inverse Fourier series 수행(Euler Integration 이용)
    end                                                 %for문 종료
    C(m)=temp/T;                                        %해당 index에 Fourier Coefficient 저장
end                                                     %for문 종료
end                                                     %함수 종료

function x=invF(C,N,t,T)                        %invF 함수 정의
w=2*pi/T;                                       %각주파수 값 설정
x=zeros(1,length(t));                           %행벡터 x 생성
for n=1:length(t)                               %t의 길이만큼 반복
    for k=-N:N                                  %k가 -N에서 N 될 때까지 반복
        x(n)=x(n)+C(k+N+1)*exp(1i*w*k*t(n));    %x(n)에 inverse Fourier series apporximation 수행
    end                                         %for문 종료
end                                             %for문 종료
end                                             %함수 종료