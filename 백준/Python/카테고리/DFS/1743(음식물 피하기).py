'''
dfs 로 가장 큰 크기를 찾는다.
'''
from collections import deque
import sys
input = sys.stdin.readline

N,M,K = map(int,input().split())
Map = [[0]*(M+1) for j in range(N+1)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

for _ in range(K):
    r,c = map(int,input().split())
    Map[r][c] = 1

def ch_in(r,c):
    if r == N+1 or c == M+1 or r<=0 or c<=0:
        return False
    return True

def dfs(r,c,n):
    need_visit = deque([[r,c]])
    while need_visit:
        print("need_visit:",need_visit)
        n+=1
        
        node = need_visit.popleft()

        Map[node[0]][node[1]] = 0

        for i in range(4):
            new_r = node[0] + dx[i]
            new_c = node[1] + dy[i]

            if not ch_in(new_r,new_c):
                continue
            if Map[new_r][new_c] == 0:
                continue
            
            
            need_visit.append([new_r,new_c])
    return n


max_count = 0
for r in range(N):
    for c in range(M):
        if Map[r][c] == 1:
            cnt = dfs(r,c,0)
            cnt = max(cnt,max_count)


print(cnt)






# from collections import deque
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(100000)
# def dfs(y,x,result):
#     result=result+1
#     M[y][x]=0
#     for _ in range(0,4):
#         ny,nx = y+ly[_], x+lx[_]
#         if 1<=ny<=n and 1<=nx<=m and M[ny][nx]==1:
#            result = result + dfs(ny,nx,0)
#     return result
    
# lx=[1,-1,0,0];ly=[0,0,1,-1]
# n,m,k = map(int, input().split())
# M = [[0]*(m+3) for _ in range(n+3)]
# for _ in range(k):
#     y,x=map(int, input().split())
#     M[y][x]=1
# ans=0
# for i in range(1,n+1):
#     for j in range(1,m+1):
#         if M[i][j]==1:
#             ans=max(ans,dfs(i,j,0))
# print(ans)
