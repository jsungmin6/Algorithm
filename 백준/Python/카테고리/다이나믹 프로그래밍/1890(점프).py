'''
bfs 로 풀었는데 메모리 초과 뜸 이유 모름

dp로 풀이
'''

import sys
input = sys.stdin.readline

N = int(input())
mat = [list(map(int,input().split())) for i in range(N)]
dp = [[-1 for i in range(N)] for j in range(N)]

def check_in(x,y):
    if x > N-1 or y > N-1:
        return False
    return True

def dfs(x,y):
    if x == N-1  and y == N-1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    x1,y1 = x+mat[x][y],y
    x2,y2 = x,y+mat[x][y]
    if check_in(x1,y1):
        dp[x][y] = dp[x][y] + dfs(x1,y1)
    if check_in(x2,y2):
        dp[x][y] = dp[x][y] + dfs(x2,y2)
    return dp[x][y]

print(dfs(0,0))

#메모리초과
# from collections import deque

# N = int(input())
# mat = [list(map(int,input().split())) for i in range(N)]
# cnt=0
# q=deque([[0,0]])
# while q:
#     x,y = q.popleft()

#     if x == N-1 and y == N-1:
#         cnt+=1
    
#     num = mat[x][y]

#     if num == 0:
#         continue

#     for new_x,new_y in [[x+num,y],[x,y+num]]:
#         if new_x > N-1 or new_y > N-1:
#             continue
#         q.append([new_x,new_y])

# print(cnt)

#바텀 업
import sys
I=sys.stdin.readline
n=int(I())
a=[]
for i in range(n):
    a+=[list(map(int,I().split()))]

b=[[0]*n for i in range(n)]
b[0][0]=1
for i in range(n):
    for j in range(n):
        t=a[i][j]
        if i+t<n:b[i+t][j]+=b[i][j]
        if j+t<n:b[i][j+t]+=b[i][j]
print(b[-1][-1]//4)