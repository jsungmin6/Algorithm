'''
bfs 2개를 따로 진행
불의 확산, 상근이의 탈출 
'''

import sys
input =sys.stdin.readline
from collections import deque

def bfs(sq,fq):
    while True:
        while sq:
            sq_size = len(sq)
            for _ in range(sq_size):
                x,y = sq.popleft()

                if Map[x][y] == -1:
                    continue

                for i in range(4):
                    new_x = x+dx[i]
                    new_y = y+dy[i]

                    if new_x < 0 or new_y < 0 or new_x == h or new_y == w:
                        return Map[x][y]+1
                    
                    if Map[new_x][new_y] !=0:
                        continue
                    
                    Map[new_x][new_y] = Map[x][y] + 1
                    sq.append([new_x,new_y])
            break

        if not sq:
            return -1
        
        while fq:
            fq_size = len(fq)
            for _ in range(fq_size):
                x,y = fq.popleft()

                for i in range(4):
                    new_x = x+dx[i]
                    new_y = y+dy[i]

                    if new_x < 0 or new_y < 0 or new_x == h or new_y == w:
                        continue
                    
                    if Map[new_x][new_y] == -1:
                        continue
                    
                    Map[new_x][new_y] = -1
                    fq.append([new_x,new_y])

            break
    

dx=[0,0,-1,1]
dy=[-1,1,0,0]

T = int(input())

for _ in range(T):
    w,h = map(int,input().rstrip().split())
    Map = [list(input()) for _ in range(h)]
    sq = deque([])
    fq = deque([])
    for i in range(h):
        for j in range(w):
            if Map[i][j] == '#':
                Map[i][j] = -1
            elif Map[i][j] == '.':
                Map[i][j] = 0
            elif Map[i][j] == '@':
                sq.append([i,j])
                Map[i][j] = 0
            else: # *
                fq.append([i,j])
                Map[i][j] = -1
    
    answer = bfs(sq,fq)
    if answer == -1:
        print('IMPOSSIBLE')
    else:
        print(answer)



