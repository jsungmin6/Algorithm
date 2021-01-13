from collections import deque

N=int(input())
graph=[[] for i in range(N+1)]
answer = [0]*(N+1)
for _ in range(N):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)
q=deque([1])
while q:
    parent=q.popleft()
    print(parent)

    if answer[parent]:
        continue
    
    for i in graph[parent]:
        answer[i]=parent
        q.append(i)

for i in range(2,N+1):
    print(answer[i])
