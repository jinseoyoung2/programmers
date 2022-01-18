# https://programmers.co.kr/learn/courses/30/lessons/17682
# https://dda0e.tistory.com/62

def solution(dartResult):
    res = []
    dartResult = dartResult.replace('10','W')
    for i in dartResult:
        if i=='W':
            res.append(10)
        elif i=='D':
            res[-1]=res[-1]**2
        elif i=='T':
            res[-1]=res[-1]**3
        elif i=='*':
            res[-1]*=2
            if len(res)!=1:
                res[-2]*=2
        elif i=='#':
            res[-1]*=(-1)
        elif i!='S':
            res.append(int(i))
    return sum(res)
