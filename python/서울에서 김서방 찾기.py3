# https://dda0e.tistory.com/9

def solution(seoul):
    A = seoul.index('Kim') # seoul에서 Kim가 몇번째 인덱스에 있는지 찾아서 저장
    answer = '김서방은 '+str(A)+'에 있다'  # str()로 A의 자료형 변환
    return answer
