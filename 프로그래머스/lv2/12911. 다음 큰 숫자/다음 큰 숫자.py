def solution(n):
    answer = 0
    cnt_n =1
    tmp_n = n
    while tmp_n > 1:
            
            if tmp_n %2 ==1:
                cnt_n+=1
            tmp_n=tmp_n//2
    while True:
        n+=1
        tmp = n
        cnt =1
        while tmp > 1:
            if tmp %2 ==1:
                cnt+=1
            tmp=tmp//2
        if cnt==cnt_n:
            answer = n
            break
    return answer