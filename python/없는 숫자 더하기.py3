# https://programmers.co.kr/learn/courses/30/lessons/86051

def solution1(numbers):
    answer = 0
    for i in range(10):
        if i not in numbers:
            answer+=i
    return answer


def solution2(numbers):
    answer = 45 - sum(numbers)
    return answer
