# https://programmers.co.kr/learn/courses/30/lessons/12922
# https://dda0e.tistory.com/45
https://dda0e.tistory.com/45?category=908549
def solution(n):
    answer = ''
    if n % 2 == 0:
        answer='수박'*(n//2)
    else:
        answer='수박'*(n//2)+'수'
    return answer
