'''
풀이
bfs로 모든 경우 탐색
'''
from collections import deque

mat = [list(map(int,input().split())) for i in range(5)]
answer_list = set()
dx,dy = [0,0,1,-1],[1,-1,0,0]

def bfs(i,j,prev):
    prev.append(mat[i][j])
    q = deque([[i,j,prev]])
    while q:
        x,y,p = q.popleft()

        if len(p) == 6:
            answer_list.add(''.join(map(str,p)))
            continue

        for l in range(4):
            new_x = x + dx[l]
            new_y = y + dy[l]

            if new_x < 0 or new_y <0 or new_x == 5 or new_y == 5:
                continue

            new_p = [k for k in p]
            new_p.append(mat[new_x][new_y])
            q.append([new_x,new_y,new_p])

for i in range(5):
    for j in range(5):
        bfs(i,j,[])

print(len(answer_list))