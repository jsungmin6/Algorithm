#유기농 배추 DFS 문제
#배열을 생성 후 배열을 0,0 부터 돌면서 몇번 dfs 가 발생하는지 체크

from collections import deque

def dfs(j,i):
    matrix[j][i]=0
    for k in range(4):
        newDx=i+dx[k]
        newDy=j+dy[k]

        if 0<=newDx and newDx<M and 0<=newDy and newDy<N and matrix[newDy][newDx]==1:
            dfs(newDy,newDx)



dx=[0,0,1,-1]
dy=[1,-1,0,0]
answer=[]
T=int(input())
for _ in range(T):
    M,N,K=map(int,input().split())
    matrix=[[0]*M for i in range(N)]

    for _ in range(K):
        x,y=map(int,input().split())
        matrix[y][x]=1


    count=0
    for i in range(M):
        for j in range(N):
            if matrix[j][i]==1:
                dfs(j,i)
                count+=1

    answer.append(count)

for i in answer:
    print(i)
