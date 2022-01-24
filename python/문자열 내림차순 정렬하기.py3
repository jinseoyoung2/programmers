# https://programmers.co.kr/learn/courses/30/lessons/12917?language=python3

def solution(s):
    answer = list(s)
    answer.sort(reverse=True)
    return "".join(answer)

def solution(s):
    return "".join(sorted(list(s), reverse=True))