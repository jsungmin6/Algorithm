'''
루트에서 가장 먼거리 찾고
거기서 또 가장 먼거리 찾기
'''
import sys
from collections import defaultdict,deque
input = sys.stdin.readline
n = int(input())
graph=defaultdict(list)
for i in range(n-1):
    a,b,w = map(int,input().split())
    graph[a].append((b,w))
    graph[b].append((a,w))

def bfs(start):
    dist = [-1]*(n+1)
    dist[start] = 0
    q =deque(graph[start])
    while q:
        node, weight = q.popleft()

        dist[node] = weight
        for nn,nw in graph[node]:
            if dist[nn] < 0 :
                q.append((nn,weight+nw))
    # print("dist : ",dist)
    return max(dist), dist.index(max(dist))
dist1, start_node = bfs(1)
dist2, last_node = bfs(start_node)
print(dist2)
