# https://programmers.co.kr/learn/courses/30/lessons/12932

def solution(n):
    answer = []
    n=str(n)
    for i in range(len(n)):
        answer.append(int(n[i]))
    answer.reverse()
    return answer