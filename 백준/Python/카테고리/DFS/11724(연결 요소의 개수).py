'''
visited 와 graph를 만들어 구하는게 아닐까
'''

from collections import deque

N,M = map(int,input().split())
visited = [0]*(N+1)
graph = [[] for i in range(N+1)]

def dfs(i):
    visited[i] = 1
    need_visit=deque(graph[i])
    while need_visit:
        node = need_visit.popleft()

        if visited[node] !=0:
            continue

        visited[node] = 1

        for k in graph[node]:
            if visited[k] !=0:
                continue
            need_visit.append(k)

for _ in range(M):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt=0
for i in range(1,N+1):
    if visited[i] != 1:
        dfs(i)
        cnt+=1

print(cnt)