n=int(input())
array=[]
for i in range(n):
    x,y=map(int,input().split(' '))
    array.append((x,y))

answer=sorted(array)

for i in answer:
    print(i[0],i[1])
