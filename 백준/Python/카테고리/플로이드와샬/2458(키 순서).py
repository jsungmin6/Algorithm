'''
풀이
플로이드 와샬을 통해 모든 경로와 이어져 있는 노드를 뽑아낸다.
'''
import sys
input = sys.stdin.readline

N,M  = map(int,input().split())
INF = 987654231
dist = [[0 if i==j else INF for i in range(N+1) ] for j in range(N+1) ]

for _ in range(M):
    a,b = map(int,input().split())
    dist[a][b] = 1


for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i ==j :
                dist[i][j] == 0
            else:
                dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])

connect=[1]*(N+1)
connect[0] = 0
for i in range(1,N+1):
    for j in range(1,N+1):
        if dist[i][j] == INF and dist[j][i] == INF:
            connect[i] = 0
            connect[j] = 0
print(sum(connect))

##dfs
import sys
input = sys.stdin.readline

def dfs(start, cur):
    if start != cur:
        edge_cnt[start] += 1
        edge_cnt[cur] += 1
    visited[cur] = True
    for w in graph[cur]:
        if not visited[w]:
            dfs(start, w)


N, M = list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
ans = 0
for _ in range(M):
    a, b = list(map(int, input().split()))
    graph[a].append(b)

edge_cnt = [0] * (N+1)
for node in range(1, N+1):
    visited = [False] * (N+1)
    dfs(node, node)

for node in range(1, N+1):
    if edge_cnt[node] == N-1:
        ans += 1

print(ans)