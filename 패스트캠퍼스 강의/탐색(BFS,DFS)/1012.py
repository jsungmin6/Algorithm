# 유기농 배추

# 풀이 방법

'''
Flood fill 문제
순서대로 dfs를 진행하며 연결된 곳은 0으로 지워준다.
지울 때마다 count를 1씩 더한 후 count 출력
'''
# # # # # # # # # # # # # # # # # # # # # 내 풀이
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def check_in(new_x, new_y):
    if new_x < 0 or new_y < 0 or new_x == M or new_y == N:
        return False
    return True


def dfs(i, j):
    mat[i][j] = 0
    for w in range(4):
        new_x = i+dx[w]
        new_y = j+dy[w]

        if check_in(new_x, new_y) and mat[new_x][new_y] == 1:
            dfs(new_x, new_y)


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    mat = [[0 for _ in range(N)] for _ in range(M)]
    for _ in range(K):
        X, Y = map(int, input().split())
        mat[X][Y] = 1

    count = 0
    for i in range(M):
        for j in range(N):
            if mat[i][j] == 1:
                count += 1
                dfs(i, j)

    print(count)
