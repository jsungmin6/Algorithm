'''
풀이
3차원 bfs 진행
'''
import sys
from collections import deque
input = sys.stdin.readline

def ch_in(z,x,y):
    if z<0 or x<0 or y<0 or z==H or x == N or y ==M:
        return False
    return True


def bfs():
    time=0
    q=deque(p_tomato)
    while q:
        q_size=len(q)
        for _ in range(q_size):
            z,x,y = q.popleft()

            for i in range(6):
                new_x=x+dx[i]
                new_y=y+dy[i]
                new_z=z+dz[i]

                if not ch_in(new_z,new_x,new_y):
                    continue
                if Map[new_z][new_x][new_y] != 0:
                    continue
                
                Map[new_z][new_x][new_y] = 1
                q.append([new_z,new_x,new_y])
        time+=1
    return time

dx=[0,0,-1,1,0,0]
dy=[-1,1,0,0,0,0]
dz=[0,0,0,0,1,-1]

M,N,H = map(int,input().split())

Map=[]
p_tomato=[]
for i in range(H):
    temp=[]
    for j in range(N):
        temp.append(list(map(int,input().split())))
    Map.append(temp)

# for i in Map:
#     print(i)

ch_no_zero=True
for h in range(H):
    for i in range(N):
        for j in range(M):
            if Map[h][i][j] == 1:
                p_tomato.append([h,i,j])
            if Map[h][i][j] == 0:
                ch_no_zero = False

if ch_no_zero:
    print(0)
    exit()

time = bfs()

ch_exist_zero = False
for h in range(H):
    for i in range(N):
        for j in range(M):
            if Map[h][i][j] == 0:
                ch_exist_zero = True
                break

# for i in Map:
#     print(i)

if ch_exist_zero:
    print(-1)
    exit()

print(time-1)

