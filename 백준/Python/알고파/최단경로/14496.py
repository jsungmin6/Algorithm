# 그대, 그머가 되어

# 풀이 과정
'''
결국 최단경로 찾으라는 문제

'''
import sys
import heapq
input = sys.stdin.readline

a, b = map(int, input().split())
N, M = map(int, input().split())
data = [list(map(int, input().split())) for i in range(M)]

graph = [[] for i in range(N+1)]

for u, v in data:
    graph[u].append(v)
    graph[v].append(u)

dist = [987654321]*(N+1)
Q = [(0, a)]

while Q:
    w, node = heapq.heappop(Q)
    if dist[node] != 987654321:
        continue
    dist[node] = w
    for v in graph[node]:
        if dist[v] != 987654321:
            continue
        alt = w+1
        heapq.heappush(Q, (alt, v))

if dist[b] == 987654321:
    print(-1)
else:
    print(dist[b])
