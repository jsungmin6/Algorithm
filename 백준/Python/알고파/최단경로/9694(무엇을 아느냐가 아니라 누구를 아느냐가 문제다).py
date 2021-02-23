'''
풀이
다익스트라
경로까지 표시 하려면 prev 배열을 추가로 구성한다.
'''
from collections import defaultdict
import sys
import heapq
input = sys.stdin.readline

INF = 10000
for c in range(int(input())):
    N,M = map(int,input().split())
    graph = defaultdict(list)
    for i in range(N):
        x,y,z = map(int,input().split())
        graph[x].append([z,y])
        graph[y].append([z,x])
    dist = [INF]*(M+1)
    prev = [-1]*(M+1)
    q=[[0,0,0]]

    while q:
        w,node,p = heapq.heappop(q)

        if dist[node] != INF:
            continue
        
        dist[node] = w
        prev[node] = p
        for nxt in graph[node]:
            nw,nv = nxt
            if dist[nv] != INF:
                continue
            nw += w
            heapq.heappush(q,[nw,nv,node])
    

    if dist[M-1] != INF:
        target = M-1
        answer = []
        while prev[target] != target:
            answer.append(target)
            target = prev[target]
        answer.append(0)
        print("Case #{0}:".format(c+1),end=" ")
        print(*answer[::-1])
    else:
        print("Case #{0}: -1".format(c+1))

###다른풀이

import heapq
input = __import__('sys').stdin.readline

def Dijkstra(start):
    dist = [float('inf')] * n
    prev = [-1]*n
    dist[start] = 0
    H = [(0,start)]
    while H:
        d, u = heapq.heappop(H)
        if dist[u] != d:
            continue
        for v, c in adj[u]:
            if dist[v] > d + c:
                dist[v] = d + c
                prev[v] = u
                heapq.heappush(H, (d + c, v))
    ans = []
    if dist[-1]==float('inf'): ans.append(-1)
    else:
        p = n-1
        while p!=-1: ans.append(p); p=prev[p]
    return reversed(ans)

for _ in range(int(input())):
    m,n = map(int,input().split())
    adj = [[] for i in range(n)]
    for i in range(m):
        a,b,c = map(int,input().split())
        adj[a].append((b,c))
        adj[b].append((a,c))
    print(f'Case #{_+1}:', *Dijkstra(0))
