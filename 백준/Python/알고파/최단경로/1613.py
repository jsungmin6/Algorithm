#  역사

# 풀이 과정
'''
여러 출발점과 도착점의 경로가 있냐 없냐를 판단하는 거기 때문에 플로이드 와샬을 사용해
dist를 전부 구한 후 판단한다. 
'''

import sys
import collections
input = sys.stdin.readline

n, k = map(int, input().split())
dist = [[0 if i == j else sys.maxsize for i in range(n+1)] for j in range(n+1)]

for _ in range(k):
    u, v = map(int, input().split())
    dist[u][v] = 1

for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

s = int(input())

for _ in range(s):
    s, e = map(int, input().split())
    if dist[s][e] == sys.maxsize and dist[e][s] == sys.maxsize:
        print(0)
    elif dist[s][e] == sys.maxsize:
        print(1)
    else:
        print(-1)
