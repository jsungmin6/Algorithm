import sys

input=sys.stdin.readline

n=int(input())
m=int(input())

num=sys.maxsize

dist = [[num for i in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a][b] = min(c, dist[a][b])

for k in range(1, n+1): 
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == j: 
                dist[i][j] = 0 
            else: 
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


for i in dist[1:]:
    for j in i[1:]:
        if j == sys.maxsize:
            print(0,end=' ')
        else:
            print(j,end=' ')
    print()

