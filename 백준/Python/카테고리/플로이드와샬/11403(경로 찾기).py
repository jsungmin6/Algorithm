'''
풀이
i에서 j로가는 경로가 있는지 확인하는 것이므로 플로이드 와샬이 적절하다.
'''
import sys
input = sys.stdin.readline

N=int(input())
dist=[]
INF = 100000
for _ in range(N):
    temp=[]
    for i in list(map(int,input().split())):
        if i == 1:
            temp.append(i)
        else:
            temp.append(INF)
    dist.append(temp)

# for i in dist:
#     print(i)

for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])

for i in dist:
    for j in i:
        if j == INF:
            print(0,end=' ')
        else:
            print(1,end=' ')
    print()
