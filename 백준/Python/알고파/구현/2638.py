# 치즈

# 풀이 방법

'''
dfs 진행하면서 1을 만나면 +1 해주고 0이면 -1 해준다.
그리고 3이상인 수와 -1을 0으로 초기화 해준다. 하고 나머지는 1로 다시 초기화 해준다.
이것을 반복한다.
'''

import sys
from collections import *
sys.setrecursionlimit(20000)
input = sys.stdin.readline
N, M = map(int, input().split())

Map = [list(map(int, list(input().split()))) for i in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def in_Map(i, j):
    if i < 0 or j < 0 or i == N or j == M:
        return False
    return True

# 치즈 녹이고 숫자 원상복구


def melt():
    for i in range(N):
        for j in range(M):
            if Map[i][j] == 1 or Map[i][j] == 2:
                Map[i][j] = 1
            else:
                Map[i][j] = 0

# 녹을 치즈 고르기


def check_melt(x, y):
    Map[x][y] = -1
    for i in range(4):
        new_x = x+dx[i]
        new_y = y+dy[i]

        if in_Map(new_x, new_y):
            if Map[new_x][new_y] == 0:
                check_melt(new_x, new_y)
            elif Map[new_x][new_y] > 0:
                Map[new_x][new_y] += 1


def end_ch(map):
    ch = True
    for row in map:
        if 1 in row:
            ch = False
            break
    return ch


time = 0
while not end_ch(Map):
    check_melt(0, 0)
    melt()
    time += 1

print(time)


# 내가 푼 방법 =>시간초과

'''
조건 포인트 : 가장자리는 치즈가 놓이지 않는다.
녹는 시간만 구하는 거면 너무 간단한 문제다.
그래서 추가된 조건이 치즈 내부에 있는 공기는 무시한다는 것.
1.시작점에서 bfs를 돌려 내부공기를 제외한 외부공기를 구한다.
2.외부공기를 제외한 모든 영역을 치즈라고 가정하고 치즈를 녹인다.
3.다시 시작점에서 bfs를 돌려서 영역을 나눈다.
4.반복
========>시간초과



# 0,0에서 시작해서 0과 1을 임의로 나눈다.
# 만약 시작전과 후가 같다면 더이상 makeMap을 할 필요가 없다.
def makeMap(map):
    newMap = [[1 for i in range(M)] for j in range(N)]
    visited = [[0 for i in range(M)] for j in range(N)]
    queue = deque([[0, 0]])
    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1
        newMap[x][y] = 0
        for i in range(4):
            new_x = x+dx[i]
            new_y = y+dy[i]

            if not in_Map(new_x, new_y):
                continue
            if visited[new_x][new_y] == 1:
                continue
            if map[new_x][new_y] == 1:
                continue

            queue.append([new_x, new_y])

    if newMap == map:
        global makeMap_ch
        makeMap_ch = False
        return newMap
    else:
        return newMap

# dfs를 돌려서 치즈를 녹여준다.


def dfs(i, j):
    visited = [[0 for i in range(M)] for j in range(N)]
    queue = deque([[i, j]])
    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1
        count = 0
        for i in range(4):
            new_x = x+dx[i]
            new_y = y+dy[i]

            if not in_Map(new_x, new_y):
                continue
            if visited[new_x][new_y] == 1:
                continue
            if Map[new_x][new_y] == 0:
                count += 1
                continue
            queue.append([new_x, new_y])
        if count > 1:
            Map[x][y] = 0


total = sum([sum(i) for i in Map])
time = 0
makeMap_ch = True
while total != 0:
    if makeMap_ch:
        newMap = makeMap(Map)
    newMap = Map

    dfs_ch = False
    for i in range(1, N-1):
        for j in range(1, M-1):
            if newMap[i][j] == 1:
                dfs(i, j)
                time += 1
                dfs_ch = True
                break
        if dfs_ch:
            break

    total = sum([sum(i) for i in Map])

print(time)
'''
