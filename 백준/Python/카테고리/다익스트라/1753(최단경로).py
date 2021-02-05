'''
풀이
다익스트라 알고리즘 으로 최단경로 구하기
경로 추적을 위해 prev 배열도 추가로 만듬
'''
from collections import defaultdict
import heapq
V,E = map(int,input().split())
K=int(input())
graph=defaultdict(list)
for _ in range(E):
    u,v,w = map(int,input().split())
    graph[u].append([w,v])

INF = 987654321
dist=[INF]*20002
prev=[-1]*(V+2)
Q=[[0,K,1]]

while Q:
    w,node,p = heapq.heappop(Q)
    if dist[node] != INF: continue
    dist[node] = w
    prev[node] = p
    for nxt in graph[node]:
        nw,nv = nxt
        if dist[nv] != INF: continue
        nw+=w
        heapq.heappush(Q,(nw,nv,node))

for i in range(1,V+1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])