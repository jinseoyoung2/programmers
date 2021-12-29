# https://programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    answer = [0,0]
    for i in range(1, len(words)):
        if (words[i] in words[0:i]) or (words[i-1][-1] != words[i][0]):
            answer=[i%n+1,i//n+1]
            break
    return answer