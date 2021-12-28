def solution(n):
    answer = 0
    A,B=0,1
    for i in range(n):
        A,B=B,A+B
    return A%1234567