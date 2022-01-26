# https://programmers.co.kr/learn/courses/30/lessons/12916?language=python3

def solution(s):
    answer = False
    s=s.lower()
    if s.count('p')==s.count('y'):
        answer = True
    return answer