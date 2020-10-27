# 꽃길

# 풀이 방법

'''
5칸의 합들을 모두 구한후 힙큐에 넣고 작은것부터 3개를 뽑음
작은 것을 넣으면서 사용한 공간을 체크하고 이 후 2번째 3번째에서 체크한 곳이면 제외함
==> 왜 틀리는지 모르겠음


'''
# # # # # # # # # # # # # # # # # # # # # 내 풀이
import sys
import heapq
input = sys.stdin.readline
N = int(input())
M = [list(map(int, input().split())) for i in range(N)]
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


def five_sum(i, j):
    total = M[i][j]
    for w in range(4):
        new_x = i+dx[w]
        new_y = j+dy[w]

        total += M[new_x][new_y]
    return total


q = []

for x in range(0, N):
    for y in range(0, N):
        if x==0 or y==0 or x==N-1 or y==N-1:
            pass
        else:
            heapq.heappush(q, (five_sum(x, y), x, y))


def check(i, j):
    ch = False
    if M[i][j] == -1:
        ch = True
    for w in range(4):
        new_x = i+dx[w]
        new_y = j+dy[w]

        if M[new_x][new_y] == -1:
            ch = True
    return ch


limit = 0
answer = 0
while limit < 3:
    total, i, j = heapq.heappop(q)
    if check(i, j):
        continue
    else:
        answer += total
        M[i][j] = -1
        for w in range(4):
            new_x = i+dx[w]
            new_y = j+dy[w]
            M[new_x][new_y] = -1
        limit += 1
print(answer)

'''
2차원 좌표를 0~N*N-1 까지 인덱스로 생각하고 전수조사.
x = flower // N
y = flower % N
이런식으로 좌표 표현
'''

# def func(lst):
#     dx, dy = [0, -1, 0, 1, 0], [0, 0, -1, 0, 1]
#     ck = []
#     result = 0

#     for flower in lst:
#         x = flower // N
#         y = flower % N

#         if x==0 or x==N-1 or y==0 or y==N-1:
#             return 10000

#         for i in range(5):
#             ck.append((x+dx[i], y+dy[i]))
#             result += pot[x+dx[i]][y+dy[i]]
            
#     if len(set(ck)) == 15:
#         return result
#     return 10000

# N = int(input())
# pot = [list(map(int, input().split())) for _ in range(N)]

# price = 10000
# for i in range(N*N):
#     for j in range(N*N):
#         for k in range(N*N):
#             lst = [i, j, k]
#             price = min(price, func(lst))
# print(price)
# '''