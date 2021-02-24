'''
풀이
1.환승을 가장적게 할 것
2.그 중에서 최단거리
그렇다면 우선순위 큐에서 꺼내는 순서를 최단거리가 아닌 먼저 환승을 제일 적게 한 것부터 꺼내야 할 듯 하다.
파이썬 heapq 는 pop 할때 배열이면 인덱스 순으로 최솟값을 구해 pop 하는 걸로 알고 있다.
배열순서는 [환승횟수, 거리, 출발지] 이다. 환승횟수가 같으면 거리가 가장 작은게 pop 될 것이다.
'''
from collections import defaultdict
import heapq
import sys
input= sys.stdin.readline
N,M = map(int,input().split())
stations,table=[],[]
graph=defaultdict(list)
INF = 1000000000
dist=[INF]*(N+1)
Q=[[0,0,0]]

for _ in range(N):
    stations.append(int(input()))
for _ in range(N):
    table.append(list(map(int,input().split())))
for i in range(N):
    for j in range(N):
        if table[i][j] != 0:
            graph[i].append([table[i][j],j])

while Q:
    r,d,v = heapq.heappop(Q)
    current_station = stations[v]

    if dist[v] != INF: continue
    
    dist[v] = d

    if v == M:
        break

    for nxt in graph[v]:
        nd,nv = nxt
        if dist[nv] != INF:
            continue
        nd += d
        if stations[nv] != current_station:
            heapq.heappush(Q,[r+1,nd,nv])
        else:
            heapq.heappush(Q,[r,nd,nv])


print(r, dist[M])