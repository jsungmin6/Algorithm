from collections import deque
import sys
input = sys.stdin.readline
T=int(input())

dx = [1,1,2,2,-1,-1,-2,-2]
dy = [-2,2,-1,1,-2,2,-1,1]


for _ in range(T):

    def ch_in(x,y):
        if x>=I or y>=I or x<0 or y<0:
            return False
        return True

    def bfs(i,j):
        visited[i][j] = True
        q=deque([[i,j]])
        count=0
        while q:
            q_size = len(q)
            
            for c in range(q_size):
                x,y = q.popleft()

                if x==ex and y==ey:
                    return count

                for k in range(8):
                    new_x = x+dx[k]
                    new_y = y+dy[k]

                    if not ch_in(new_x,new_y):
                        continue
                    if visited[new_x][new_y]:
                        continue

                    visited[new_x][new_y] = True

                    q.append([new_x,new_y])
            
            count+=1

        return count


    I = int(input())
    sx,sy = map(int,input().split())
    ex,ey =  map(int,input().split())

    Map = [[0 for i in range(I)] for j in range(I)]
    visited = [[False for i in range(I)] for j in range(I)]

    print(bfs(sx,sy))


