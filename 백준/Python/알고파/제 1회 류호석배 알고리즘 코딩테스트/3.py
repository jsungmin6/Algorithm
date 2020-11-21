# 2번 - 문자열 지옥에 빠진 호석

# 풀이 과정
'''
dfs응용일듯 싶다.
'''

import sys
sys.setrecursionlimit(2000) # 재귀스택깊이 조절
input=sys.stdin.readline
N,M,K = map(int,input().split());
Map = [list(input().rstrip()) for i in range(N)]

dx=[-1, -1, -1, 0, 1, 1, 1, 0]
dy=[-1, 0, 1, 1, 1, 0, -1, -1]

def dfs(i,j,t):
    global count
    find_str = data[t] # 다음으로 찾아야 할 문자
    for k in range(8):
        new_x = j+dx[k]
        new_y = i+dy[k]

        new_x%=M
        new_y%=N

        if Map[new_y][new_x] == find_str: 
            if t==len(data)-1: #찾는 문자중 마지막 문자였다면 count +1을 해준다.
                count+=1
                continue
            dfs(new_y,new_x,t+1)

for _ in range(K):
    count = 0
    data = list(input().rstrip())
    if len(data) == 1: # 문자가 1개일 경우
        for i in range(N):
            for j in range(M):
                if data[0] == Map[i][j]:
                    count+=1
    else:
        for i in range(N):
            for j in range(M):
                if data[0] == Map[i][j]:
                    dfs(i,j,1)
    print(count)





