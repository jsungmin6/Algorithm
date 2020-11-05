import collections
import heapq
import sys

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
datas = [list(map(int, input().split())) for _ in range(E)]

graph = collections.defaultdict(list)
for u, v, w in datas:
    graph[u].append((v, w))

Q = [(0, K)]
dist = collections.defaultdict(int)

while Q:
    time, node = heapq.heappop(Q)
    if node not in dist:
        dist[node] = time
        for v, w in graph[node]:
            alt = time + w
            heapq.heappush(Q, (alt, v))

for i in range(1, V+1):
    if i == K:
        print(0)
    else:
        if dist[i] == 0:
            print('INF')
        else:
            print(dist[i])

# 블루코드

input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())
datas = [list(map(int, input().split())) for _ in range(E)]
graph = [[] for _ in range(20005)]
for u, v, w in datas:
    graph[u].append((v, w))
Q = [(0, K)]
dist = [987654321 for i in range(20005)]
dist[K] = 0
while Q:
    time, node = heapq.heappop(Q)
    for v, w in graph[node]:
        if dist[v] > dist[node] + w:
            heapq.heappush(Q, (dist[node] + w, v))
            dist[v] = dist[node] + w
for i in range(1, V+1):
    if dist[i] == 987654321:
        print('INF')
    else:
        print(dist[i])

# 블루코드 개선
import heapq
import sys
input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())
datas = [list(map(int, input().split())) for _ in range(E)]
graph = [[] for _ in range(20005)]
for u, v, w in datas:
    graph[u].append((v, w))
Q = [(0, K)]
dist = [987654321 for i in range(20005)]
while Q:
    time, node = heapq.heappop(Q)

    if dist[node] != 987654321:
        continue

    dist[node] = time

    for v, w in graph[node]:
        if dist[v] != 987654321:
            continue
        heapq.heappush(Q, (dist[node] + w, v))

for i in range(1, V+1):
    if dist[i] == 987654321:
        print('INF')
    else:
        print(dist[i])
