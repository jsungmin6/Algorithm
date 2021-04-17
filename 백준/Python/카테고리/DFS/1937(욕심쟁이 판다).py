'''
풀이
dp 메모이제이션을 통해 dp[i][j] = i,j에서 가장 오래 살수 있는 날로 초기화
가장 오래 살 수 있는 날은 dfs를 통해 구한다.
'''

import sys
from collections import deque
sys.setrecursionlimit(40000)
input = sys.stdin.readline

n = int(input())
mat = [list(map(int,input().split())) for i in range(n)]
dx,dy = [0,0,1,-1],[-1,1,0,0]
answer = 0
dp = [[-1 for i in range(n)] for j in range(n)]

def isin(x,y):
    if -1<x<n:
        if -1<y<n: return True
    return False

def dfs(x,y):
    global answer, dp

    if dp[x][y] != -1: return dp[x][y]

    temp = 0
    dp[x][y] = 1

    for i in range(4):
        new_x, new_y = x+dx[i],y+dy[i]

        if isin(new_x,new_y):
            if mat[new_x][new_y] > mat[x][y]:
                temp = max(temp,dfs(new_x,new_y))
        
    dp[x][y] += temp

    if answer < dp[x][y]: answer = dp[x][y]

    return dp[x][y]

for i in range(n):
    for j in range(n):
        dfs(i,j)

print(answer)
        