# 뿌요뿌요

# 풀이 방법

'''
유기농 배추와 마찬가지로 모든칸을 0~9까지 단계가 진행될 때마다 돌려준다.
K 이상인 범위를 발견했을 때 지워준다.
밑에 0이 있다면 내려준다.
반복 => 지우는게 없을 때 끝

함수를 나눠서 처리하고, check box를 만들어서 체크한곳을 다시 체크하지 않게 주의가 필요하다. 안 그러면 무한루프를 계속 돈다.

왜 틀렸나 계속 봤는데 0을 '0'으로 안 처리한게 하나 있었다.
근데 에러는 다른곳에서 계속 터져서 시간이 오래 걸렸다.
틀렸을 때 디버깅 하는 연습이 많이 필요할 듯.


'''
# # # # # # # # # # # # # # # # # # # # # 내 풀이
import sys
sys.setrecursionlimit(100000)

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


def in_M(i, j):
    if i < 0 or j < 0 or i >= N or j >= 10:
        return False
    return True

def dfs_num(i, j):
    ch_num[i][j] = True
    ret = 1
    for w in range(4):
        new_x = i+dx[w]
        new_y = j+dy[w]

        if not in_M(new_x, new_y):
            continue
        if M[new_x][new_y] != M[i][j] or ch_num[new_x][new_y]:
            continue

        ret += dfs_num(new_x, new_y)

    return ret

def dfs_remove(i, j, val):
    M[i][j] = '0'
    ch_remove[i][j] = True
    for w in range(4):
        new_x = i+dx[w]
        new_y = j+dy[w]

        if not in_M(new_x, new_y):
            continue
        if M[new_x][new_y] != val or ch_remove[new_x][new_y]:
            continue

        dfs_remove(new_x, new_y, val)


def down():
    for j in range(10):
        temp = []
        for i in range(N):
            if M[i][j] != '0':
                temp.append(M[i][j])
        zero_temp = ['0']*(N-len(temp))
        zero_temp.extend(temp)
        for i in range(N):
            M[i][j] = zero_temp[i]


N, K = map(int, input().split())
M = [list(input()) for _ in range(N)]

while True:
    exist = False
    ch_num = [[False for i in range(10)] for _ in range(N)]
    ch_remove = [[False for i in range(10)] for _ in range(N)]
    for i in range(N):
        for j in range(10):
            if M[i][j] == '0' or ch_num[i][j]:
                continue
            num = dfs_num(i, j)
            if num >= K:
                dfs_remove(i, j, M[i][j])
                exist = True
    if not exist:
        break

    down()

for i in M:
    print(''.join(i))
