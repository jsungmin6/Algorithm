'''
풀이
플로이드 와샬 알고리즘 사용
'''
import sys
input = sys.stdin.readline

n=int(input())
m=int(input())
INF = 1000000000
dist=[[INF for i in range(n+1)] for j in range(n+1)]

for i in range(n+1):
    dist[i][i] = 0

#전처리 단계
for _ in range(m):
    a,b,c = map(int,input().split())
    dist[a][b] = min(dist[a][b], c);

#플로이드 와샬 알고리즘
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == j:
                dist[i][j]= 0
            else:
                dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j]);

for i in dist[1:]:
    for j in i[1:]:
        if j == INF:
            print(0,end=' ')
        else:
            print(j,end=' ')
    print()



