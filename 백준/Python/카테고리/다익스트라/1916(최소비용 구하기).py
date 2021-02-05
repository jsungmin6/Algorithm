'''
풀이
최단거리 다익스트라
'''
from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline
N=int(input())
M=int(input())
graph=defaultdict(list)
for _ in range(M):
    u,v,w = map(int,input().split())
    graph[u].append([w,v])

s,e=map(int,input().split())
INF = 100000000000

dist=[INF]*(N+2)
Q=[[0,s]]

while Q:
    time,node = heapq.heappop(Q)

    if dist[node] != INF:
        continue
    
    dist[node] = time

    for w,v in graph[node]:
        if dist[v] != INF:
            continue
        nw = time+w
        heapq.heappush(Q,[nw,v])

print(dist[e])