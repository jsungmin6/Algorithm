n=int(input())

books={}
for _ in range(n):
    book=input()
    if book in books:
        books[book]+=1
    else:
        books[book]=1

maxnum=max(books.values())
array=[]

for book,number in books.items():
    if number == maxnum:
        array.append(book)

print(sorted(array)[0])
