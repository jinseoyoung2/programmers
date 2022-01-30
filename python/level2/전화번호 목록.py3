# https://dda0e.tistory.com/18
    
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]) : # A.startswith(B) => A가 B로 시작하는지의 여부를 알려줌
            return False
    return True
