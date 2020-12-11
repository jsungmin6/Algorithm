'''
그래프 component의 수를 세는 문제.
모든 배열을 돌면서 몇번의 dfs가 실행되었는지 수를 세면 된다.
'''

import sys
input = sys.stdin.readline
T=int(input())


dx=[0,0,-1,1]
dy=[-1,1,0,0]

def in_range(i,j):
    if i==N or j==M or i<0 or j < 0:
        return False
    return True

def dfs(i,j):
    need_visit=[[i,j]]
    while need_visit:
        x,y = need_visit.pop()

        Map[x][y] = 0

        for i in range(4):
            new_x = x+dx[i]
            new_y = y+dy[i]

            if not in_range(new_x,new_y):
                continue
            
            if Map[new_x][new_y] == 0:
                continue
            
            need_visit.append([new_x,new_y])
    

for _ in range(T):
    M,N,K = map(int,input().split())
    Map = [[0 for i in range(M+1)] for j in range(N+1)]
    
    #배추밭 
    for _ in range(K):
        y,x = map(int,input().split())
        Map[x][y] = 1
    
    cnt=0
    for i in range(N):#세로
        for j in range(M):#가로
            if Map[i][j] == 1:
                dfs(i,j)
                cnt+=1

    print(cnt)