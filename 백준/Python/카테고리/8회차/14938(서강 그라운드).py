'''
플로이드 와샬을 통해 i 지점에서 j 지점으로 가는 최단거리들을 모두 구한후
각 행의 m 이하의 값들을 찾아 계산 한 후 최대값을 찾는다.
'''

import sys
input = sys.stdin.readline

n,m,r = map(int,input().split())
items = list(map(int,input().split()))
graph = [[] for i in range(n+1)]
INF = 987654321

dist = [[0 if i==j else INF for i in range(n+1)] for j in range(n+1)]

for i in range(r):
    a,b,l = map(int,input().split())
    if dist[a][b] > l:
        dist[a][b] = l
    if dist[b][a] > l:
        dist[b][a] = l

for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            if i==j:
                dist[i][j] = 0
            else:
                dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])

max_items = 0
for i in range(1,n+1):
    temp = 0
    for j in range(1,n+1):
        if dist[i][j] <= m:
            temp+=items[j-1]
    max_items = max(max_items,temp)
print(max_items)