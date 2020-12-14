'''
이분탐색은 정렬되어 있지 않아 불가
dfs 모두 시도
'''
from collections import deque
import sys
sys.setrecursionlimit(20000)
input = sys.stdin.readline

def ch_in(r,c):
    if r==N or c==N or r<0 or c<0:
        return False
    return True

def dfs(x,y,d):
    visited[x][y] = True
    for i in range(4):
        new_x = x+dx[i]
        new_y = y+dy[i]

        if not ch_in(new_x,new_y):
            continue
        if visited[new_x][new_y]:
            continue
        if Map[new_x][new_y] <= d:
            continue
        
        dfs(new_x,new_y,d)



N=int(input())

Map = [list(map(int,input().split())) for i in range(N)]


dx=[0,0,1,-1]
dy=[-1,1,0,0]

hi = max([max(i) for i in Map])
lo = min([min(i) for i in Map])
answer = 1 # 최소 1개

for i in range(lo,hi):
    visited = [[False for i in range(N)] for j in range(N)]
    cnt=0
    for r in range(N):
        for c in range(N):
            if Map[r][c] > i and not visited[r][c]:
                dfs(r,c,i)
                cnt+=1
    answer=max(answer,cnt)

print(answer)
