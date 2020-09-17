N,I=map(int,input().split())
array=[]
for _ in range(N):
    array.append(input())

array.sort()
print(array[I-1])
