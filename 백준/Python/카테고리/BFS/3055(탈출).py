'''
bfs 두개 따로 진행
'''
from collections import deque

R,C = map(int,input().split())

Map = [list(input()) for _ in range(R)]

flood = deque([])
GSD = deque([])

for i in range(R):
    for j in range(C):
        if Map[i][j] == '.':
            Map[i][j] = 1
        elif Map[i][j] == 'D':
            Map[i][j] = 1
            bx,by = i,j
        elif Map[i][j] == 'S':
            Map[i][j] = 0
            GSD.append([i,j]) 
        elif Map[i][j] =='*':
            Map[i][j] = 0
            flood.append([i,j])
        elif Map[i][j] == 'X':
            Map[i][j] = 0

dx=[0,0,1,-1]
dy=[-1,1,0,0]
count=0

while GSD:
    count+=1
    GSD_temp = deque([])
    flood_temp= deque([])

    #홍수 이동
    while flood:
        fx,fy = flood.popleft()
        for i in range(4):
            new_x = fx + dx[i]
            new_y = fy + dy[i]

            if new_x == bx and new_y ==by: #비버소굴 이동 못함
                continue
            if new_x <0 or new_y <0 or new_x == R or new_y ==C: # 범위 밖
                continue
            if Map[new_x][new_y] == 0: # 이미 홍수 or 돌
                continue

            
            Map[new_x][new_y] = 0
            flood_temp.append([new_x,new_y])

    #고슴도치 이동
    while GSD:
        x,y = GSD.popleft()
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]

            if new_x == bx and new_y ==by:
                print(count)
                exit()
            
            if new_x <0 or new_y <0 or new_x == R or new_y ==C:
                continue

            if Map[new_x][new_y] == 0 or Map[new_x][new_y] > 1:
                continue
            
            Map[new_x][new_y] = count
            GSD_temp.append([new_x,new_y])
    
    GSD = GSD_temp
    flood = flood_temp
print('KAKTUS')
    
    

