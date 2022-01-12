# https://programmers.co.kr/learn/courses/30/lessons/82612?language=python3

def solution(price, money, count):
    answer = 0
    for i in range(1, count+1):
        answer+=price*i
    if answer-money<=0:
        answer=0
    else:
        answer=answer-money
    return answer
