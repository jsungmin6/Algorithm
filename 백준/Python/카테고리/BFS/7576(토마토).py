from collections import deque

M,N = map(int,input().split())
Map = [list(map(int,input().split())) for _ in range(N)]


dx =[0,0,-1,1]
dy =[-1,1,0,0]

def ch_in(x,y):
    if x==N or y==M or x<0 or y<0:
        return False
    return True

def bfs(tomatos):
    count=0
    while tomatos:
        for _ in range(len(tomatos)):
            x,y = tomatos.popleft()

            for i in range(4):
                new_x = x+dx[i]
                new_y = y+dy[i]

                if not ch_in(new_x,new_y) or Map[new_x][new_y] != 0:
                    continue
            
                Map[new_x][new_y] = Map[x][y] +1
                tomatos.append([new_x,new_y])
        count+=1
    return count



tomatos=deque([])
for i in range(N):
    for j in range(M):
        if Map[i][j] == 1:
            tomatos.append([i,j])

answer = bfs(tomatos)

for i in range(N):
    for j in range(M):
        if Map[i][j] == 0:
            print(-1)
            exit()

print(answer-1)
