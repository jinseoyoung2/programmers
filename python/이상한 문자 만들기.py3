# https://programmers.co.kr/learn/courses/30/lessons/12930?language=python3

def solution(s):
    s = s.split(' ')
    res = []
    for i in range(len(s)):
        x = []
        for j in range(len(s[i])):
            if j%2==0:
                x.append(s[i][j].upper())
            else:
                x.append(s[i][j].lower())
        res.append("".join(x))
    return " ".join(res)