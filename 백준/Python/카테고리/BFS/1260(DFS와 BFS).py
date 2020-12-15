
from collections import deque
N,M,V = map(int,input().split())

graph=[[] for i in range(N+1)]

for _ in range(M):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(V):
    visited=[-1]*(N+1)
    q=deque([V])
    answer=[]
    while q:
        node = q.popleft()
        if visited[node] == 1:
            continue
        answer.append(node)
        visited[node] = 1

        next_graph = sorted(graph[node])
        for i in next_graph:
            if visited[i] == -1:
                q.append(i)
                
    return answer

def dfs(V):
    visited=[-1]*(N+1)
    need_visited = [V]
    answer=[]
    while need_visited:
        node = need_visited.pop()
        if visited[node] == 1:
            continue
        answer.append(node)
        visited[node] = 1

        next_graph = sorted(graph[node],reverse=True)
        for i in next_graph:
            if visited[i] == -1:
                need_visited.append(i)
                
    return answer


for i in dfs(V):
    print(i,end=' ')
print()
for i in bfs(V):
    print(i,end=' ')