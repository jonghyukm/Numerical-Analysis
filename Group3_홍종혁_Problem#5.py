#Problem5
x = float(input("Input any positive real number : "))    #양의 실수 x를 입력받음
p = 1;q=1    #초기값 설정
while 1:    #while문으로 무한 반복 수행
    p = (q + x/q)/2    # Newton square-root algorithm 식
    if q==p:break    # q와 p가 같을 시 반복문 종료
    q = p    #q에 p 저장
print(f'approximation of root of x is {p}')  #p를 출력한다. 이는 square root of x의 근사값이다.
print(f'√x = {x**0.5}')    #실제 값과 비교하기 위해 실제 값 출력