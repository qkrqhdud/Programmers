def solution(n):
    answer= 0 
    fibo=[]
    fibo.append(0)
    fibo.append(1)

    for cnt in range(2,n+1):
        fibo.append(fibo[cnt-1] % 1234567+ fibo[cnt-2] % 1234567)
    answer = fibo[n] % 1234567
    return answer
