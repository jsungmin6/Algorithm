# 특정 거리의 도시 찾기

# 풀이 과정
'''
모든 도시의 최단거리를 찾고 일치하는 최단거리를 출력하는 것이기 때문에
다익스트라 알고리즘을 사용해서 출발지점으로부터 모든 도시의 최단거리를 찾는다.
'''
import sys
import collections
import heapq
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
datas = [list(map(int, input().split())) for _ in range(M)]

graph = collections.defaultdict(list)

for u, v in datas:
    graph[u].append(v)


dist = collections.defaultdict(int)

Q = [(0, X)]

answer = []

while Q:
    weight, node = heapq.heappop(Q)
    if node not in dist:
        if weight == K:
            heapq.heappush(answer, node)
        dist[node] = weight

        for v in graph[node]:
            alt = weight+1
            heapq.heappush(Q, (alt, v))

if not answer:
    print(-1)
else:
    for i in range(len(answer)):
        print(heapq.heappop(answer))
