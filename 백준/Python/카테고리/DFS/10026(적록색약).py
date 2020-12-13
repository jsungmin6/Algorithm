'''
dfs 두번
첫 dfs 에서 G 개수 찾고 G를 R로 바꿈
두번째에서 R과 B를 0으로 바꾸면서 dfs
'''

import sys
from copy import deepcopy
sys.setrecursionlimit(20000)

dx=[0,0,-1,1]
dy=[-1,1,0,0]
N = int(input())
Map = [list(input()) for i in range(N)]
Map2 = deepcopy(Map)

for i in range(N):
    for j in range(N):
        if Map2[i][j] =='G':
            Map2[i][j] = 'R'

def ch_in(x,y):
    if x==N or y==N or x<0 or y<0:
        return False
    return True

def dfs(r,c,Map):
    target = Map[r][c]
    Map[r][c] = 0
    for i in range(4):
        new_r = r + dx[i]
        new_c = c + dy[i]

        if not ch_in(new_r,new_c):
            continue
        if Map[new_r][new_c] != target:
            continue

        dfs(new_r,new_c,Map)

RnBnG = 0
for r in range(N):
    for c in range(N):
        if Map[r][c] != 0:
            dfs(r,c,Map)
            RnBnG+=1

RnB = 0
for r in range(N):
    for c in range(N):
        if Map2[r][c] != 0:
            dfs(r,c,Map2)
            RnB+=1

print(RnBnG,RnB)