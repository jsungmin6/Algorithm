'''
풀이
루트노드를 찾고
루트에서 가장 멀리 떨어진 정점 찾고
가장 멀리 떨어진 정점에서 가장 먼 거리를 찾는다.
'''
import sys
from collections import defaultdict,deque
input = sys.stdin.readline

V = int(input())
#인접리스트 그래프 구현 
graph = defaultdict(list)
for i in range(V):
    temp = list(map(int,input().split()))
    v = temp[0]
    data = temp[1:-1]
    for j in range(0,len(data),2):
        u,w = data[j],data[j+1]
        graph[v].append([u,w])

def bfs(start):
    dist=[-1]*(V+1)
    dist[start] = 0
    q = deque(graph[start])
    while q:
        node, weight = q.popleft()

        dist[node] = weight

        for nn,nw in graph[node]:
            if dist[nn] < 0:
                q.append([nn,nw+weight])
    return max(dist), dist.index(max(dist))

_, start_node = bfs(1)
answer,end_node = bfs(start_node)
print(answer)