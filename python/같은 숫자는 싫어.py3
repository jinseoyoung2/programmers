def solution(arr):
    answer = []
    for i in range(len(arr)): # arr리스트의 요소 개수 만큼 반복
        if i==0:
            answer.append(arr[0]) # append()를 사용하여 answer에 값 넣기
        elif arr[i-1]!=arr[i]:
            answer.append(arr[i])
    return answer
