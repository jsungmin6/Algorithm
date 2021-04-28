'''
풀이
파이프를 위 행부터 시작해서 빵집 위행이랑 연결되도록 한다.
'''
import sys
from collections import deque 
input = sys.stdin.readline
R, C = map(int,input().split())
mat = [list(input().rstrip()) for i in range(R)]
visited = [[0 for i in range(C)] for j in range(R)]
def bfs(n):
    global visited
    q = deque([[n,0]])
    while q:
        x,y = q.pop()
        visited[x][y] = 1
        if y == C-1:
            return True

        for nx,ny in [[x+1,y+1],[x,y+1],[x-1,y+1]]:
            if 0 <= nx < R and 0 <= ny < C:
                if mat[nx][ny] != 'x' and not visited[nx][ny]:
                    
                    q.append([nx,ny])

cnt = 0
for i in range(R):
    if bfs(i):
        cnt+=1
    # for j in visited:
    #     print(j)
    # print()
print(cnt)