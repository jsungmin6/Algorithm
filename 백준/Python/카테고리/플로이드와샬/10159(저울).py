'''
풀이
플로이드 와샬로 이어져 있어서 비교가 가능한지 확인 가능ㅇ
dfs를 통해서도 가능
'''

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
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

for i in range(1,N+1):
    cnt=0
    for j in range(1,N+1):
        if dist[i][j] == INF and dist[j][i] == INF:
            cnt+=1
    print(cnt)