import heapq,sys
input = sys.stdin.readline

N,M,X = map(int,input().split())
INF = 987654321
graph = [[] for i in range(N+1)]
graph_reverse = [[] for i in range(N+1)]

for _ in range(M):
    s,e,w = map(int,input().split())
    graph[s].append([w,e])
    graph_reverse[e].append([w,s])

def dijkstra(graph,X):
    dist = [INF for i in range(N+1)]
    pq=[[0,X]]

    while pq:
        w,s = heapq.heappop(pq)

        if dist[s] != INF:
            continue

        dist[s] = w

        for nw,nn in graph[s]:
            if dist[nn] != INF:
                continue
            heapq.heappush(pq,[w+nw,nn])
    
    return dist

dist = dijkstra(graph,X)
dist_rev = dijkstra(graph_reverse,X)
answer = 0
for i in range(1,N+1):
    s = dist[i] + dist_rev[i]
    answer = max(s,answer)
print(answer)