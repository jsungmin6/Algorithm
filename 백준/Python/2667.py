N=int(input())
data=[]
for _ in range(N):
    k=input()
    temp=[]
    for i in k:
        temp.append(int(i))
    data.append(temp)

array=[]
num=0
def dfs(i,j):
    if data[i][j]==1:
        data[i][j]=0
        global num
        num+=1
        if i<N-1:
            dfs(i+1,j)
        if j<N-1:
            dfs(i,j+1)
        if i>0:
            dfs(i-1,j)
        if j>0:
            dfs(i,j-1)
    return num

count=0

for i in range(N):
    for j in range(N):
        if data[i][j]==1:
            array.append(dfs(i,j))
            num = 0
            count+=1

print(count)
array.sort()
for i in array:
    print(i)
