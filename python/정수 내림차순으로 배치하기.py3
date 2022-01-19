def solution(n):
    answer = 0
    listN=list(map(int, str(n)))
    listN.sort(reverse=True)
    for i in listN:
        answer = answer*10+i
    return answer