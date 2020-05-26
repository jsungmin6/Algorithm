n=int(input())
m=int(input())

array=[[] for _ in range(n+1)]
switch=[0]*(n+1)


for i in range(m):
    x,y=map(int,input().split())
    array[x].append(y)
    array[y].append(x)

def dfs(i):
    switch[i]=1
    for j in array[i]:
        if not(switch[j]):
            dfs(j)

dfs(1)
print(switch.count(1)-1)
