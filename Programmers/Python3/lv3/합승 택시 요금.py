'''
풀이
S,A,B 를 시작점으로 하는 다익스트라를 3번한다.
각 최단거리의 합의 최솟값을 구한다.

'''
n=6
s=4
a=6
b=2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]


import heapq

INF = 987654321

def f(graph,s,n):
    dist = [INF]*(n+1)
    pq = [[0,s]]

    while pq:
        w,v = heapq.heappop(pq)

        if dist[v] != INF:
            continue
        
        dist[v] = w

        for nv,nw in graph[v]:
            if dist[nv] != INF:
                continue
            heapq.heappush(pq,[w+nw,nv])
    
    return dist

def solution(n, s, a, b, fares):
    graph = [[] for i in range(n+1)]
    
    for fare in fares:
        start,end,w = fare
        graph[start].append([end,w])
        graph[end].append([start,w])

    dist_s = f(graph,s,n)
    dist_a = f(graph,a,n)
    dist_b = f(graph,b,n)

    answer = 987654321
    for i in range(1,n+1):
        answer = min(answer,dist_s[i]+dist_a[i]+dist_b[i])

    return answer

print(solution(n, s, a, b, fares))