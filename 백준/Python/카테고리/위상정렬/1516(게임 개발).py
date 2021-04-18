'''
풀이
위상정렬
'''
from collections import deque

N = int(input())
time = [0]
result = [0] * (N+1)
graph = [[] for i in range(N+1)]
indegree = [0 for i in range(N+1)]
q = deque()

for i in range(1,N+1):
    temp = list(map(int,input().split()))
    time.append(temp[0])
    ad = temp[1:-1]
    if ad:
        for a in ad:
            graph[a].append(i)
            indegree[i] +=1

for i in range(1,N+1):
    if indegree[i] == 0:
        result[i] = time[i]
        q.append(i)

for i in range(N):
    cur = q.popleft()
    for n in graph[cur]:
        result[n] = max(result[n],result[cur] + time[n])
        indegree[n] -=1
        if indegree[n] == 0: q.append(n)

for i in range(1,N+1):
    print(result[i])