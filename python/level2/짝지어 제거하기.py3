# https://programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    answer=0
    stack=[]
    for i in range(len(s)):
            if len(stack)==0:
                stack.append(s[i])
            else:
                if s[i]==stack[-1]:
                    stack.pop()
                else:
                    stack.append(s[i])
    if len(stack)==0: answer=1
    return answer
