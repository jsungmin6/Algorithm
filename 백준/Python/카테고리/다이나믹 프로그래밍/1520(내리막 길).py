'''
풀이
bfs => 모든 경로에 +1씩 해주는 방법 => 시간초과
dfs
'''
import sys
from collections import deque
input = sys.stdin.readline

M,N = map(int,input().split())
mat = [list(map(int,input().split())) for i in range(M)]
dp = [[-1 for i in range(N)] for j in range(M)]
dx,dy = [0,0,1,-1], [-1,1,0,0]

def ch_in(x,y):
    if x<0 or y<0 or x==M or y==N:
        return False
    return True

# def bfs():
#     q = deque([[0,0]])
#     while q:
#         x,y = q.popleft()

#         for i in range(4):
#             nx,ny = x+dx[i],y+dy[i]

#             if not ch_in(nx,ny):
#                 continue
#             if mat[nx][ny] >= mat[x][y]:
#                 continue
            
#             dp[nx][ny] +=1

#             q.append([nx,ny])

# def dfs(x,y):
#     if x==M-1 and y ==N-1:
#         return 1
#     if dp[x][y] != -1:
#         return dp[x][y]
#     dp[x][y] = 0
#     for i in range(4):
#         nx,ny = x+dx[i],y+dy[i]

#         if ch_in(nx,ny):
#             if mat[nx][ny] < mat[x][y]:
#                 dp[x][y] += dfs(nx,ny)
#     for l in dp:
#         print(l)
#     print()
#     return dp[x][y]


def dfs2(x, y):
    if x == 0 and y == 0:
        return 1
    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if ch_in(nx,ny):
                if mat[x][y] < mat[nx][ny]:
                    dp[x][y] += dfs2(nx, ny)
    for l in dp:
        print(l)
    print()
    return dp[x][y]

print(dfs2(M-1,N-1))
