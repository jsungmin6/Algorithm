'''
dfs로 깊이 탐색
중복 알파벳 백트래킹
'''

import sys
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


R, C = map(int, input().split())
Map = [list(input().rstrip()) for _ in range(R)]
visited = [[0 for i in range(C)] for j in range(R)]
used = []
cnt = 0
result = 0


def ch_in(x, y):
    if x == R or y == C or x < 0 or y < 0:
        return False
    return True


def back(x, y, cnt):
    global result
    result = max(result, cnt)
    visited[x][y] = 1
    used.append(Map[x][y])
    for i in range(4):
        new_x = x+dx[i]
        new_y = y+dy[i]

        if not ch_in(new_x, new_y):
            continue
        if visited[new_x][new_y] == 1:
            continue
        if Map[new_x][new_y] in used:
            continue

        back(new_x, new_y, cnt+1)

    visited[x][y] = 0
    used.pop()


back(0, 0, 1)
print(result)

##다른풀이
import sys

# 좌, 하, 우, 상
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def BFS(x, y):
    global answer
    q = set([(x, y, board[x][y])])

    while q:
        x, y, ans = q.pop()

        # 좌우상하 갈 수 있는지 살펴본다
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # index 벗어나지 않는지 체크하고, 새로운 칸이 중복되는 알파벳인지 체크한다
            if ((0 <= nx < R) and (0 <= ny < C)) and (board[nx][ny] not in ans):
                q.add((nx,ny,ans + board[nx][ny]))
                answer = max(answer, len(ans)+1)


R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]

answer = 1
BFS(0, 0)
print(answer)