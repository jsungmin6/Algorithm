#백트래킹 풀이 시도 -> 시간초과

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
graph = [[] for i in range(N+1)]
for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt=0
visited=[0]*(N+1)
v=[]
def sol(com):
    global cnt
    if len(com) == 3:
        k=sorted(com)
        temp=''.join(map(str,k))
        if temp in v:
            return
        v.append(temp)
        cnt+=1
        return
    
    for i in range(1,N+1):

        ch=False
        for j in graph[i]:
            if j in com:
                ch=True
                break
        if ch:
            continue
        if visited[i] == 1:
            continue
        com.append(i)
        visited[i] = 1
        sol(com)
        com.pop()
        visited[i] = 0

sol([])
print(cnt)

##for문 으로 풀이
N, M = map(int, input().split())
cnt = 0
if N < 3:
    print(cnt)
else:
    unmixed = {i: [] for i in range(1, N+1)}
    for _ in range(M):
        i, j = map(int, input().split())
        unmixed[i].append(j)
        unmixed[j].append(i)

    for i in range(1, N+1):
        for j in range(i+1, N+1):
            if j in unmixed[i]:
                continue
            for k in range(j+1, N+1):
                if k in unmixed[i] or k in unmixed[j]:
                    continue
                cnt += 1
    print(cnt)

#dfs 이용한 탐색
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
matrix = {name:list() for name in range(n+1)}
for _ in range(m):
    x, y = map(int, input().split())
    matrix[x].append(y)
    matrix[y].append(x)
def dfs(s, n, c):
    if s > n:
        return 0
    elif len(c) == 3:
        return 1
    else:
        count = 0
        for i in range(s+1,n+1):
            vector = list()
            for x in c:
                vector += matrix[x]
            if i not in vector:
                count += dfs(i,n,c+[i])
        return count
print(dfs(0,n,[]))