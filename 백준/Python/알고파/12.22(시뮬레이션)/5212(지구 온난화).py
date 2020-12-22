'''
for 문 돌면서 X찾고 주면에 .이 3개 이상이면 후보에 추가
후보들을 돌면서 .으로 바꿔줌.
'''

R, C = map(int, input().split())
Map = []
for _ in range(R):
    Map.append(list(input()))

dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


cd = []
for i in range(R):
    for j in range(C):
        if Map[i][j] == 'X':
            cnt = 0
            for k in range(4):
                new_i = i+dx[k]
                new_j = j+dy[k]

                if new_i < 0 or new_j < 0 or new_i == R or new_j == C:
                    cnt += 1
                    continue

                if Map[new_i][new_j] == '.':
                    cnt += 1
            if cnt >= 3:
                cd.append([i, j])


for x, y in cd:
    Map[x][y] = '.'


min_x = R
max_x = 0
min_y = C
max_y = 0
for x in range(R):
    for y in range(C):
        if Map[x][y] == 'X':
            min_x = min(min_x, x)
            max_x = max(max_x, x)
            min_y = min(min_y, y)
            max_y = max(max_y, y)


for i in Map[min_x:max_x+1]:
    print(''.join(i[min_y:max_y+1]))
