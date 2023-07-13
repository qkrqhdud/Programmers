def solution(s):
    answer = -1
    list_s = ['0']
    for i in s:
        if list_s[-1] == i:
            list_s.pop()
        else:
            list_s.append(i)
  # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    if len(list_s)==1:
        return 1
    else:
        return 0


    return answer