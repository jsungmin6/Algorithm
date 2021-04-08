'''
dfs를 방문하지 않은 모든 나라에 적용한다.
dfs를 통해 조건에 맞는 인접한 나라 들을 구한 후 평균을 구하고 값을 대입한다.
check함수를 통해 끝이 났는지 체크

개선점
다시 한바퀴 돌때는 평균냈던 좌표를 다시 돌 필요는 없다
'''

import sys
from collections import deque
input = sys.stdin.readline



# 두 좌표의 값 차이
def diff(x1,y1,x2,y2): 
    return abs(mat[x1][y1] - mat[x2][y2])

# 동서남북 방향으로 확장 할 수 있는지
def connect(i,j):
    for t in range(4):
        new_x = i+dx[t]
        new_y = j+dy[t]

        if new_x<0 or new_y<0 or new_x == n or new_y ==n:
            continue

        #차이가 l 이상 r이하여야 국경이 열린다.
        if l <= diff(new_x,new_y,i,j) and diff(new_x,new_y,i,j) <= r: 
            return True
    return False

# 모든 국경이 닫혔는지 확인
def isFinish(mat): 
    global n,l,r;
    for i in range(n):
        for j in range(n):
            if connect(i,j):
                return False
    return True

#받은 좌표를 평균으로 바꿈
def change_mat(prev):
    if len(prev) == 1:
        return
    temp = []
    for x,y in prev:
        temp.append(mat[x][y])
    
    mid = sum(temp)//len(temp)

    for x,y in prev:
        mat[x][y] = mid

def dfs(i,j):
    visited[i][j] = 1
    q = deque([[i,j]])
    prev = []
    prev.append([i,j])
    while q:
        x,y = q.pop()

        for t in range(4):
            new_x = x+dx[t]
            new_y = y+dy[t]

            if new_x<0 or new_y<0 or new_x == n or new_y ==n:
                continue
            if visited[new_x][new_y]:
                continue
            if l > diff(new_x,new_y,x,y) or diff(new_x,new_y,x,y) > r:
                continue

            visited[new_x][new_y] = 1
            prev.append([new_x,new_y])
            q.append([new_x,new_y])
    return prev

dx=[0,0,1,-1]
dy=[1,-1,0,0]

n,l,r = map(int,input().split())
mat = [list(map(int,input().split())) for i in range(n)]

cnt = 0
#국경을 한번씩 열고 확인 
while not isFinish(mat):
    cnt+=1
    visited = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]: 
                #바꿀 좌표들을 받음
                prev = dfs(i,j)
                # print("i,j : ",i,j)
                # print("prev :",prev)
                #좌표를 평균으로 값을 바꿈
                change_mat(prev)
    # for ma in mat:
    #     print(ma)


print(cnt)