# 운동

# 풀이 과정
'''
자기 자신으로 돌아오는 경로 중  최소인 거리 구하기.
모든 경로 구하는거니 플로이드 와샬
자기자신으로 돌아오는 경로이므로 dist[i][i] 인 부분만 체크
'''

import sys
import collections
input = sys.stdin.readline

V, E = map(int, input().split())

dist = [[sys.maxsize for i in range(V+1)] for j in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    dist[u][v] = w

for k in range(V+1):
    for i in range(V+1):
        for j in range(V+1):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

array = []
for i in range(V+1):
    if dist[i][i] != sys.maxsize:
        array.append(dist[i][i])

if not array:
    print(-1)
else:
    print(min(array))
