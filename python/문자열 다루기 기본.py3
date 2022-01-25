# https://programmers.co.kr/learn/courses/30/lessons/12918

def solution(s):
    answer = False
    if len(s)==4 or len(s)==6:
        answer = s.isdigit()
    return answer