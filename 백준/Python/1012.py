import sys
sys.setrecursionlimit(100000)

t=int(input())


def dfs(i,j):
    if array[i][j]==1:
        array[i][j]=0
        if i<n-1:
            dfs(i+1,j)
        if j<m-1:
            dfs(i,j+1)
        if i>0:
            dfs(i-1,j)
        if j>0:
            dfs(i,j-1)

for _ in range(t):
    count=0
    m,n,k=map(int,input().split())
    array=[[0]*m for _ in range(n)]
    for _ in range(k):
        x,y=map(int,input().split())
        array[y][x]=1
    for i in range(n):
        for j in range(m):
            if array[i][j]==1:
                dfs(i,j)
                count+=1
    print(count)
