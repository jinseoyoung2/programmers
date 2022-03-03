# https://programmers.co.kr/learn/courses/30/lessons/12969

w, h = map(int, input().split(' ')) # 공백을 기준으로 나눠 정수형으로 저장
for i in range(h):
    for j in range(w):
        print('*', end='')
    print()
