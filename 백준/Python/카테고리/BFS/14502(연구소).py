'''
풀이
1.랜덤하게 0을 1로 바꿀 3곳 찾기
2.바이러스 퍼트리기
3.안전구역 크기 찾기
반복
'''

import sys
from copy import deepcopy
from collections import deque
input = sys.stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]

N,M = map(int,input().split())
Map,virus = [],[]
answer=0

for _ in range(N):
    Map.append(list(map(int,input().split())))

for i in range(N):
    for j in range(M):
        if Map[i][j] == 2:
            virus.append([i,j])

def wall(c):
    if c == 3:
        bfs()
        return
    else:
        for i in range(N):
            for j in range(M):
                if Map[i][j] == 0:
                    Map[i][j] = 1
                    wall(c+1)
                    Map[i][j] = 0

def ch_in(x,y):
    if x < 0 or y < 0 or x == N or y == M:
        return False
    return True

def bfs():
    v = deepcopy(virus)
    q = deque(v)
    safe=0
    global answer

    temp_map = deepcopy(Map)

    while q:
        x,y = q.popleft()

        for i in range(4):
            new_x = x+dx[i]
            new_y = y+dy[i]

            if not ch_in(new_x,new_y):
                continue
            if temp_map[new_x][new_y] != 0:
                continue
            
            temp_map[new_x][new_y] = 2
            q.append([new_x,new_y])
    
    # for i in temp_map:
    #     print(i)
    # print()

    for i in range(N):
        for j in range(M):
            if temp_map[i][j] == 0:
                safe+=1
    
    answer = max(answer,safe)

wall(0)
print(answer)



#다른 풀이
maze_ori, b, ans = [], [], 0
N, M = map(int, input().split())
for row in range(N): maze_ori += list(map(int, input().split()))
for i in range(N * M):
	if maze_ori[i] == 0: b.append(i)

for i in range(len(b) - 2):
	for j in range(i + 1, len(b)):
		for k in range(j + 1, len(b)):

			maze = maze_ori[:]
			maze[b[i]], maze[b[j]], maze[b[k]] = 1, 1, 1
			queue = []
			for v in range(N * M):
				if maze[v] == 2: queue.append(v)

			for v in queue:
				if maze[v] == 2:
					U, R, D, L = v - M, v + 1, v + M, v - 1
					if maze[U] == 0 and U >= 0: maze[U] = 2; queue.append(U)
					if R < N * M and maze[R] == 0 and R % M : maze[R] = 2; queue.append(R)
					if D < N * M and maze[D] == 0: maze[D] = 2; queue.append(D)
					if maze[L] == 0 and L % M != M - 1: maze[L] = 2; queue.append(L)

			safe = maze.count(0)
			if ans < safe: ans = safe

print(ans)
