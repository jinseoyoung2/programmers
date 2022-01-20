# https://programmers.co.kr/learn/courses/30/lessons/12948

def solution(phone_number):
    answer = list(phone_number)
    for i in range(len(answer)-4):
        answer[i]='*'
    return "".join(answer)
