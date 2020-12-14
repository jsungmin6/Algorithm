n=int(input())
a,b= map(int,input().split())
m=int(input())

from collections import deque

graph=[[] for i in range(n+1)]

for _ in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

# print("graph:",graph)
visited=[False for i in range(n+1)]
def bfs(i):
    q=deque([i])
    level=0
    while q:
        q_size = len(q)
        for j in range(q_size):
            node = q.popleft()
            visited[node] = True
            if node == b:
                return level          
            for k in graph[node]:
                if not visited[k]:
                    q.append(k)
        level+=1
    return -1

print(bfs(a))
