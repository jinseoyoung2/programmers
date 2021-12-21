def solution(s): 
    answer = ''
    if len(s)%2==1: # len() 함수로 s의 문자 개수를 구해 2로 나눈 값이 1일 경우 홀수
        answer=s[len(s)//2]
    else: # len() 함수로 s의 문자 개수를 구해 2로 나눈 값이 1이 아닐 경우 짝수
        answer=s[len(s)//2-1:len(s)//2+1]
    return answer
