# https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    answer=[]
    for i in range(1, yellow+1):
        if yellow%i==0:
            a=yellow//i
            if 2*(a+i)+4==brown:
                answer=[i+2,a+2]
    return answer