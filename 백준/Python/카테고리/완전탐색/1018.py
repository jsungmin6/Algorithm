# 체스판 다시 칠하기

'''
W로 시작할때와 B로 시작할 때를 구분해야함.
'''

import sys
N, M = map(int, input().split())
Map = [input() for i in range(N)]


def check(u, v):
    a = 0
    b = 0
    for i in range(u, u+8):
        for j in range(v, v+8):
            if (i+j) % 2 == 0:
                if Map[i][j] == 'B':
                    a += 1
                else:
                    b += 1
            else:
                if Map[i][j] == 'W':
                    a += 1
                else:
                    b += 1
    return min(a, b)


min_num = sys.maxsize
for i in range(N-7):
    for j in range(M-7):
        num = check(i, j)
        min_num = min(min_num, num)

print(min_num)
