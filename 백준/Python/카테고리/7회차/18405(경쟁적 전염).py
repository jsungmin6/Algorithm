'''
풀이

bfs로 순서대로 진행
'''
from collections import deque

N,K = map(int,input().split())
mat = [list(map(int,input().split())) for i in range(N)]
S,X,Y = map(int,input().split())
dx=[0,0,1,-1]
dy=[1,-1,0,0]
start = [] # 바이러스 종류, x,y좌표

for i in range(N):
    for j in range(N):
        if mat[i][j] != 0:
            start.append([mat[i][j],i,j])

start.sort()

visited = [[0 for i in range(N)] for j in range(N)]
for i in start:
    kind,tx,ty = i
    visited[tx][ty] = kind
q = deque(start)

cnt=0
while q:
    q_size = len(q)
    cnt+=1
    if cnt == S+1:
        break
    for _ in range(q_size):
        kind,tx,ty = q.popleft()

        for i in range(4):
            nx = tx+dx[i]
            ny = ty+dy[i]

            if nx<0 or nx == N or ny<0 or ny == N:
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = kind
                q.append([kind,nx,ny])

print(visited[X-1][Y-1])

    

