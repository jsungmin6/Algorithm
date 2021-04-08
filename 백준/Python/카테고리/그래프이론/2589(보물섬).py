'''
땅좌표에서 전부 최장거리를 찾아 리턴한다.
'''
from collections import deque
import sys
input = sys.stdin.readline

r,c= map(int,input().split())
mat = [list(input().rstrip()) for i in range(r)]
spot = []

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def dist_all(i,j):
    visited = [[0 for i in range(c)] for j in range(r)]
    q= deque([[i,j]])
    visited[i][j] = 1
    cnt = 0
    while q:
        q_size = len(q)
        cnt+=1
        for _ in range(q_size):
            x,y = q.popleft()
            for l in range(4):
                new_x,new_y = x+dx[l],y+dy[l]

                if new_x<0 or new_y <0 or new_x == r or new_y == c:
                    continue
                if visited[new_x][new_y]:
                    continue
                if mat[new_x][new_y] == "W":
                    continue
                
                visited[new_x][new_y] = 1
                q.append([new_x,new_y])
    
    return cnt 

answer=0
for i in range(r):
    for j in range(c):
        if mat[i][j] == 'L':
            answer = max(dist_all(i,j),answer)
            
print(answer-1)
