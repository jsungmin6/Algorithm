n=int(input())
array=[]
left=1
right=1
index=0
for _ in range(n):
    array.append(int(input()))

for i in range(0,len(array)-1):
    if(array[index]<array[i+1]):
        left+=1
        index=i+1

index=len(array)-1
for i in range(len(array)-1,0,-1):
    if(array[index]<array[i-1]):
        right+=1
        index=i-1


print(left,right)
