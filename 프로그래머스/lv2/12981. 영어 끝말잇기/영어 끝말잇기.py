# import math

# def solution(n, words):
#     answer = []
#     valid = []
#     ans=[]
#     for word in words:
#         turn = math.ceil((len(valid)+1)/n)
#         cnt = n - (len(valid)+1)% n
#         if len(word)==1:
#             answer.append(cnt)
#             answer.append(turn)
#             print(valid[-1][-1],word[0])
#             return answer       
#         if word in valid:
#             answer.append(cnt)
#             answer.append(turn)
#             return answer
#         if len(valid)==0:
#             valid.append(word)
#         else:    
            
#             if valid[-1][-1] == word[0]:   
#                 valid.append(word)
#             else:
#                 answer.append(cnt)
#                 answer.append(turn)
#                 return answer
        
#     answer = [0,0]
#     # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.

#     return answer

def solution(n, words):
    answer = [0,0]
    stack = [words[0]]
    for i in range(1, len(words)):
        if stack[-1][-1] == words[i][0] and words[i] not in stack and len(words[i])!=1:
            stack.append(words[i])
        else:
            answer[0] = (i % n) + 1
            answer[1] = i // n + 1
            break
    return answer