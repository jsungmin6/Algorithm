def dfs(i):
    global count
    for j in array[i]:
        count+=1
        dfs(j)


from collections import deque

def bfs(v):
    q=deque([v])
    visited=[False]*(n+1)
    visited[v]=True
    count=1
    while q:
        v = q.popleft()
        for e in array[v]:
            if not visited[e]:
                q.append(e)
                visited[e]=True
                count+=1
    return count

n,m=map(int,input().split())
array=[[] for _ in range(n+1)]
countlist=[[] for _ in range(n+1)]
for _ in range(m):
    b,a=map(int,input().split())
    array[a].append(b)

for i in range(n+1):
    x = bfs(i)
    countlist[i]=x

index=-1
for i in countlist:
    index+=1
    if i==max(countlist):
        print(index,end=" ")
