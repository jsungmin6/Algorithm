'''
3차원 bfs
'''

from collections import deque
import sys
input =sys.stdin.readline

dx=[0,0,1,-1,0,0]
dy=[-1,1,0,0,0,0]
dz=[0,0,0,0,1,-1]
def ch_in(x,y,z):
    if x==L or y==R or z==C or x<0 or y<0 or z<0:
        return False
    return True

def bfs(SL,SR,SC,EL,ER,EC,Map):
    q = deque([[SL,SR,SC]])
    while q:
        x,y,z = q.popleft()
 
        for i in range(6):
            new_x = x+dx[i]
            new_y = y+dy[i]
            new_z = z+dz[i]

            if not ch_in(new_x,new_y,new_z):
                continue
            if Map[new_x][new_y][new_z] != 1 or Map[new_x][new_y][new_z] == '0':
                continue
            
            Map[new_x][new_y][new_z] = Map[x][y][z]+1
            if new_x==EL and new_y == ER and new_z == EC:
                return Map[new_x][new_y][new_z]
            
            q.append([new_x,new_y,new_z])
    return -1


while True:

    
    L,R,C = map(int,input().split())
    #종료
    if L==0 and R==0 and C==0:
        break

    Map=[]
    visited=[[[-1 for i in range(C)] for j in range(R)] for k in range(L)]
    S=[-1,-1,-1]
    E=[-1,-1,-1]
    for l in range(L):
        floor = [list(input().rstrip()) for i in range(R)]

        #S찾기
        if S[0] == -1 or E[0] == -1:
            for r in range(R):
                for c in range(C):
                    if floor[r][c] == 'S':
                        floor[r][c] = 0
                        S[0] = l
                        S[1] = r;
                        S[2] = c;
                    if floor[r][c] == 'E':
                        floor[r][c] = 1
                        E[0] = l
                        E[1] = r;
                        E[2] = c;
                    if floor[r][c] == '.':
                        floor[r][c] = 1
                    if floor[r][c] == '#':
                        floor[r][c] = 0

        Map.append(floor)
        input() # 공백 줄 제거
    
    answer = bfs(S[0],S[1],S[2],E[0],E[1],E[2],Map)

    if answer ==-1:
        print("Trapped!")
    else:
        print("Escaped in {} minute(s).".format(answer))

    # for i in Map:
    #     for j in i:
    #         print(j)
    #     print()
    # print()

