'''
풀이
시뮬레이션
'''

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
mat = [list(map(int,input().split())) for i in range(N)]
move = [list(map(int,input().split())) for i in range(M)]
dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]


def new_change(x,y,d,s):
    nx = (x + ((dx[d-1] + N)*s)%N)%N
    ny = (y + ((dy[d-1] + N)*s)%N)%N
    return nx,ny

def move_cloud(sx,sy,d,s):
    dix,diy = dx[d-1],dy[d-1]
    if sx+(dix*s) < 0:
        nx = (N-(abs(sx+(dix*s)) % N))%N
    else:
        nx = (sx+(dix*s)) % N
    if sy+(diy*s) < 0:
        ny = (N-(abs(sy+(diy*s)) % N))%N
    else:
        ny = (sy+(diy*s)) % N
    return nx,ny

def cloud_start(x,y):
    result = [[x,y]]
    for i,j in [[0,1],[1,1],[1,0]]:
        nx = (x+i)%N
        ny = (y+j)%N
        result.append([nx,ny])
    return result

def rain(clouds):
    for x,y in clouds:
        mat[x][y] +=1

def water_copy(clouds):
    for x,y in clouds:
        cnt=0
        for i,j in [[-1,-1],[1,1],[1,-1],[-1,1]]:
            nx = x+i
            ny = y+j
            if nx<0 or nx == N or ny<0 or ny == N:
                continue
            if mat[nx][ny]:
                cnt+=1
        mat[x][y] += cnt

def empty_bucket(clouds):
    temp = []
    for i in range(N):
        for j in range(N):
            if mat[i][j] >=2 and [i,j] not in clouds:
                mat[i][j] -= 2
                temp.append([i,j])
    return temp

def total_water():

    return sum([sum(ele) for ele in mat])

clouds = cloud_start(N-2,0)
for d,s in move:
    temp = [] 
    for x,y in clouds:
        cx, cy = new_change(x,y,d,s)
        temp.append([cx,cy])

    rain(temp)

    water_copy(temp)

    clouds = empty_bucket(temp)

print(total_water())






