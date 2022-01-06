# https://programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    st = ['zero','one','two','three','four','five','six','seven','eight','nine']
    for i in range(len(st)):
        if st[i] in s:
            s = s.replace(st[i], str(i))
    answer=int(s)
    return answer