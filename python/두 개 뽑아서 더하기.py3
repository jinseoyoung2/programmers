def solution(numbers):
    answer = []
    for i in range(0, len(numbers)):
        for j in range(0, len(numbers)):
            plus = numbers[i]+numbers[j]
            if j!=i and plus not in answer:
                answer.append(plus)
    answer.sort()
    return answer