'''
몇 단계 가야 하는지
최단 경로 찾기
bfs
'''
from collections import deque

N,M = map(int,input().split())
Map = [list(map(int,list(input()))) for i in range(N)]

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def ch_in(x,y):
    if x==N or y==M or x<0 or y<0:
        return False
    return True

def bfs(i,j):
    q=deque([[i,j]])
    while q:
        x,y = q.popleft()

        for k in range(4):
            new_x = x+dx[k]
            new_y = y+dy[k]
            
            if not ch_in(new_x,new_y):
                continue
            if Map[new_x][new_y] != 1:
                continue
            
            
            Map[new_x][new_y] = Map[x][y]+1
            q.append([new_x,new_y])

bfs(0,0)

print(Map[N-1][M-1])