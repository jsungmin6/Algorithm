'''
dfs 로 탐색하면서 컴포넌트 수와 cnt 반환
단, 그림이 하나도 없는 경우에는 가장 넓은 그림의 넓이는 0이다.
'''

import sys
input = sys.stdin.readline
n,m = map(int,input().split())
mat = [list(map(int,input().split())) for i in range(n)]
visited = [[0]*m for i in range(n)]
total,mx = 0,0

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def check_in(x,y):
    if x<0 or y<0 or x==n or y==m:
        return False
    return True

def dfs(i,j):
    cnt=1
    visited[i][j] = 1
    stack = [[i,j]]
    while stack:
        x,y =  stack.pop()
        
        for l in range(4):
            new_x = x+dx[l]
            new_y = y+dy[l]

            if not check_in(new_x,new_y):
                continue
            if visited[new_x][new_y]:
                continue
            if mat[new_x][new_y] == 0:
                continue
            
            visited[new_x][new_y] = 1
            cnt+=1
            stack.append([new_x,new_y])

    return cnt

for i in range(n):
    for j in range(m):
        if not visited[i][j] and mat[i][j] == 1:
            total+=1
            mx = max(mx,dfs(i,j))


print(total)
print(mx)
    
