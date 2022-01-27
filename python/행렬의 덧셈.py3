# https://programmers.co.kr/learn/courses/30/lessons/12950?language=python3
# https://dda0e.tistory.com/83

def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j]+=arr2[i][j]
    return arr1
