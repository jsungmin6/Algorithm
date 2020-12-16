'''
Map에 변수를 하나 더 추가함
변수는 내가 현재 벽을 부순 상태인지 아닌지를 판단하는 수
'''

from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
Map = [list(map(int,list(input().rstrip()))) for _ in range(N)]
visited = [[[False,0] for i in range(M)] for j in range(N)]
dx=[0,0,1,-1]
dy=[-1,1,0,0]

def ch_in(x,y):
    if x<0 or y<0 or x==N or y==M:
        return False
    return True

def bfs():
    q = deque([[0,0,0]])

    visited[0][0] = [True,0]
    count=1
    while q:
        q_size = len(q)
        for _ in range(q_size):
            x,y,crash = q.popleft()


            for i in range(4):
                new_x = x + dx[i]
                new_y = y + dy[i]

                if new_x == N-1 and new_y == M-1:
                    return count+1
                
                if not ch_in(new_x,new_y):
                    continue


                # print('input:',new_x,new_y,crash)

                if crash==0 and visited[new_x][new_y]==[True,0]:
                    continue
                
                if crash==1 and visited[new_x][new_y][0]:
                    continue

                if crash == 1 and Map[new_x][new_y] == 1:
                    continue

                # print('sorting:',new_x,new_y,crash)

                if crash == 0 and Map[new_x][new_y] == 1:
                    q.append([new_x,new_y,1])
                    visited[new_x][new_y] = [True,1]
                else:
                    q.append([new_x,new_y,crash])
                    visited[new_x][new_y] = [True,crash]
        count+=1
    return -1

if N==1 and M ==1:
    if Map[0][0] == 0:
        print(1)
    else:
        print(-1)
    exit()

print(bfs())


#다른풀이 좀 깔끔 방법은 같음
import sys
I = sys.stdin.readline
def bfs(r,c):
    que = [(0,0,False)]
    count = 1
    while que:
        que_ = []
        for r,c,flag in que:
            if r == R-1 and c == C-1:
                return count
            for dr, dc in dir:
                rr = r + dr
                cc = c + dc
                if 0 <= rr < R and 0 <= cc < C:
                    if not flag:
                        if not visitF[rr][cc]:
                            if Map[rr][cc] == '0':
                                visitF[rr][cc] = True
                                que_.append((rr,cc,False))
                            else:
                                visitF[rr][cc] = True
                                que_.append((rr,cc,True))
                    else:
                        if not visitT[rr][cc]:
                            if Map[rr][cc] == '0':
                                visitT[rr][cc] = True
                                que_.append((rr,cc,True))
        
        que = que_
        count += 1
    return -1

dir = [[1,0], [-1,0], [0,1], [0,-1]]
R, C = list(map(int, I().split()))
Map = [list(I()) for _ in range(R)]
visitF = [[False] * C for _ in range(R)]
visitT = [[False] * C for _ in range(R)]

print(bfs(0,0))
