'''
알고리즘
2차원 격자에서 #으로 갖혀있는 영역을 체크해야 한다.
dfs

풀이과정
모든 좌표를 dfs하며 dfs한번 실행할때마다 안에서 늑대와 양의 수를 센 후 계산해서 리턴한다.
#q에 넣기 전에 조건을 넣어 더 걸러주는것이 시간이 줄어든다.

시간복잡도
O(V+E)
'''


import sys
from collections import deque

def check_in(x,y):
    if x<0 or y<0 or x==R or y ==C:
        return False
    return True  

def dfs(i,j):
    
    in_wolf = 0
    in_sheep = 0

    if Map[i][j] == 'v':
        in_wolf+=1
    elif Map[i][j] =='o':
        in_sheep+=1
    Map[i][j] = '#'
    q=deque([[i,j]])
    while q:
        x,y = q.popleft()

        for k in range(4):
            new_x = x+dx[k]
            new_y = y+dy[k]

            if not check_in(new_x,new_y):
                continue
            
            if Map[new_x][new_y] == '#':
                continue
            
            if Map[new_x][new_y] == 'v':
                in_wolf+=1
            elif Map[new_x][new_y] =='o':
                in_sheep+=1

            Map[new_x][new_y] = '#'

            q.append([new_x,new_y])
    
    if in_wolf >= in_sheep:
        in_sheep=0
    else:
        in_wolf=0
    

    return [in_wolf,in_sheep]


input= sys.stdin.readline
wolf = 0
sheep = 0

dx = [0,0,1,-1]
dy = [1,-1,0,0]

R,C = map(int,input().split())
Map=[list(input().rstrip()) for _ in range(R)]


for i in range(R):
    for j in range(C):
        if Map[i][j] != '#':
            in_wolf,in_sheep = dfs(i,j)
            wolf+=in_wolf
            sheep+=in_sheep

print(sheep,wolf)


    