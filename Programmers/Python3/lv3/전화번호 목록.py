'''
풀이
길이순으로 정렬 후 이후 문자열을 짧은 길이의 문자열만큼 슬라이싱 해서 같은게 있는지 확인 
'''
phone_book=["119", "97674223", "1195524421"]
def solution(phone_book):
    phone_book.sort(key=lambda x: len(x))
    book_num=len(phone_book)
    for i in range(book_num):
        for j in range(i+1,book_num):
            if phone_book[i]==phone_book[j][:len(phone_book[i])]:
                return False    
    return True

print(solution(phone_book))