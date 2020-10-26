# 늑대와 양

# 풀이 방법

'''
늑대 주변에 양이 있는지만 체크하면 끝
나머지 칸을 D로 채워서 제출
'''
# # # # # # # # # # # # # # # # # # # # # 내 풀이
R, C = map(int, input().split())
M = [list(input()) for i in range(R)]

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

ch = False
for i in range(R):
    for j in range(C):
        if M[i][j] == 'W':
            for w in range(4):
                new_x = i+dx[w]
                new_y = j+dy[w]

                if new_x < 0 or new_y < 0 or new_x == R or new_y == C:
                    continue

                if M[new_x][new_y] == 'S':
                    ch = True

if ch:
    print(0)
else:
    print(1)
    for i in range(R):
        for j in range(C):
            if M[i][j] == '.':
                M[i][j] = 'D'
    for i in M:
        print(''.join(i))
