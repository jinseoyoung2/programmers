# https://programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    answer = ''
    test = '~!@#$%^&*()=+[{]}:?,<>/'
    #1단계
    new_id = new_id.lower()
    #2단계
    for i in new_id:
        if i not in test:
            answer+=i
    #3단계
    while '..' in answer:
        answer = answer.replace('..', '.')
    #4단계
    if answer[0]=='.': answer = answer[1:]
    if len(answer)>1 and answer[-1]=='.': answer = answer[:-1]
    #5단계
    if len(answer)<1: answer='a'
    #6단계
    if len(answer)>=16: 
        answer = answer[:15]
        if answer[-1]=='.': answer = answer[:-1]
    #7단계
    while len(answer)<3:
        answer+=answer[-1]
    return answer
