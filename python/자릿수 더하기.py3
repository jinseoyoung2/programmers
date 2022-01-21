# https://programmers.co.kr/learn/courses/30/lessons/12931

def solution(n):
    N=str(n)
    answer=0
    for i in range(len(N)):
        answer+=int(N[i])
    return answer