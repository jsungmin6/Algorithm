'''
string 변환해서 돌과 킹 좌표찾기
맵 그리기
시뮬레이션 돌리기
돌만났을 경우, 벽 만났을 경우 처리
'''

K, S, N = input().split(' ')
dic = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7}
K_y = dic[K[0]]
K_x = 8-int(K[1])
S_y = dic[S[0]]
S_x = 8-int(S[1])

chess = [[0 for i in range(8)] for j in range(8)]
# print('K : ', K_x, K_y)
# print('S : ', S_x, S_y)
k_move = {'R': [0, 1], 'L': [0, -1], 'B': [1, 0], 'T': [-1, 0],
          'RT': [-1, 1], 'LT': [-1, -1], 'RB': [1, 1], 'LB': [1, -1]}
for _ in range(int(N)):
    i = input()
    x, y = k_move[i]

    K_x = K_x+x
    K_y = K_y+y

    if K_x < 0 or K_y < 0 or K_x == 8 or K_y == 8:
        K_x -= x
        K_y -= y
        continue

    if K_x == S_x and K_y == S_y:
        S_x = S_x+x
        S_y = S_y+y

        if S_x < 0 or S_y < 0 or S_x == 8 or S_y == 8:
            K_x -= x
            K_y -= y
            S_x -= x
            S_y -= y
            continue
    # print('K : ', K_x, K_y)
    # print('S : ', S_x, S_y)

for key, value in dic.items():
    if value == K_y:
        print(key, end='')
        print(str(8-K_x))

for key, value in dic.items():
    if value == S_y:
        print(key, end='')
        print(str(8-S_x))
