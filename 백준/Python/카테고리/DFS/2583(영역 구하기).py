'''
dfs
'''
import sys
input = sys.stdin.readline
import heapq
sys.setrecursionlimit(20000)

M,N,K = map(int,input().split())

Map = [[1 for i in range(N)] for j in range(M)]

for _ in range(K):
    x1,y1,x2,y2 = map(int,input().split())
    x1 = x1
    x2 = x2-1
    y1,y2 = M-y2, M-y1-1

    for r in range(y1,y2+1):
        for c in range(x1,x2+1):
            Map[r][c] = 0


dx = [0,0,-1,1]
dy = [-1,1,0,0]

def ch_in(x,y):
    if x== M or y == N or x < 0 or y < 0:
        return False
    return True

def dfs(r,c):
    Map[r][c] = 0
    cnt = 1
    for i in range(4):
        new_r = r+dx[i]
        new_c = c+dy[i]

        if not ch_in(new_r,new_c):
            continue
        if Map[new_r][new_c] == 0:
            continue

        cnt += dfs(new_r,new_c)

    return cnt


answer = []
for r in range(M):
    for c in range(N):
        if Map[r][c] == 1:
            cnt = dfs(r,c)
            heapq.heappush(answer,cnt)

print(len(answer))
while answer:
    print(heapq.heappop(answer), end = ' ')



##스택 풀이

import sys
M,N,K = map(int, sys.stdin.readline().split())
g = [[0]*M for _ in range(N)]
for _ in range(K):
    frmx, frmy, tox, toy = map(int, sys.stdin.readline().split())

    for x in range(frmx, tox):
        for y in range(frmy, toy):
            g[x][y] = 1

land = []

def dfs(x,y):
    count = 1
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]

    g[x][y] = 1
    stack = [(x,y)]

    while stack:
        x,y = stack.pop()
        for i in range(4):
            nxtx = x+dx[i]
            nxty = y+dy[i]

            if 0<=nxtx<N and 0<=nxty<M and g[nxtx][nxty] == 0:
                g[nxtx][nxty] = 1
                stack.append((nxtx, nxty))
                count += 1

    land.append(count)

for i in range(N):
    for j in range(M):
        if g[i][j] == 0:
            dfs(i,j)

land.sort()
print(len(land))
print(" ".join(str(x) for x in land))