# https://programmers.co.kr/learn/courses/30/lessons/12947
# https://dda0e.tistory.com/86

def solution(x):
    xlist = list(str(x))
    N=0
    for i in xlist:
        N+=int(i)
    if x%N==0:
        return True
    else:
        return False
