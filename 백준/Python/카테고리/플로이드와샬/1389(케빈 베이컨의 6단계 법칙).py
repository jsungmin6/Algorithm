'''
풀이
플로이드 와샬
'''
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
INF = 100000
dist=[[INF for i in range(N+1)] for j in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    dist[a][b] = 1
    dist[b][a] = 1

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i==j:
                dist[i][j] = 0
            else:
                dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])

kevin_num=[INF]
min_num=INF
for i in dist[1:]:
    total = sum(i[1:])
    kevin_num.append(total)
    min_num = min(min_num,total)

print(kevin_num.index(min_num))
