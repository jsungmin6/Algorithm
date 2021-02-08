'''
풀이
다익스트라를 3번 해서 총합을 구하면 될 것 같다. 한번 이동했던 간선을 다시 이동할 수 있다는 조건이 이 풀이를 사용하라는 뜻 같다.
'''
from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

def dk(s,e,graph):#시작지점, 목적지
    dist=[INF]*(N+1)
    Q = [[0,s]]
    while Q:
        weight, node = heapq.heappop(Q)

        if dist[node] != INF:
            continue
        
        dist[node] = weight

        for w,v in graph[node]:
            if dist[v] != INF:
                continue
            aw=w+weight
            heapq.heappush(Q,[aw,v])

    return dist[e] if dist[e] != INF else -1

N,E= map(int,input().split())
graph=defaultdict(list)

for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append([c,b])
    graph[b].append([c,a])

v1,v2 = map(int,input().split())
INF = 9876543210

s_to_v1=dk(1,v1,graph)
v1_to_v2=dk(v1,v2,graph)
v2_to_e=dk(v2,N,graph)
if  s_to_v1== -1 or v1_to_v2 == -1 or v2_to_e== -1:
    print(-1)
    exit()

s_to_v2=dk(1,v2,graph)
v2_to_v1=dk(v2,v1,graph)
v1_to_e=dk(v1,N,graph)
if  s_to_v2== -1 or v2_to_v1 == -1 or v1_to_e== -1:
    print(-1)
    exit()

print(min(s_to_v1+v1_to_v2+v2_to_e,s_to_v2+v2_to_v1+v1_to_e))


