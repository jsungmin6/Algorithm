n=int(input())
array=[]
for _ in range(n):
    array.append(int(input()))

array.sort()

count=0
index=1
for i in array:
    count+=abs(index-i)
    index+=1

print(count)
