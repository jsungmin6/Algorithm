#나이트의 이동

#풀이계획

#BFS
#이차원 배열을 만듬
#나이트 이동가능 데이터 배열 만들기
#BFS돌리기

###############################################################

from collections import deque

#나이트 이동경로
dx=[-2,-2,-1,-1,1,1,2,2]
dy=[1,-1,2,-2,2,-2,1,-1]

answer=[]
N=int(input())

for _ in range(N):
    line=int(input())
    sx,sy=map(int,input().split())
    ex,ey=map(int,input().split())


    chess=[[0]*line for i in range(line)]

    #BFS
    need_visit=deque([[sx,sy]])
    chess[sx][sy]=0
    while need_visit:
        x,y=need_visit.popleft()

        #queue에서 들어온 노드가 도착지점일 경우
        if x==ex and y==ey:
            answer.append(chess[x][y])
            break

        #나이트 이동경로 8군데를 큐에 추가해주고 몇 번째 단계인지 표시
        for i in range(8):
            newX=x+dx[i]
            newY=y+dy[i]
            if newX>=0 and newY>=0 and newX<line and newY<line and chess[newX][newY]==0:
                need_visit.append([newX,newY])
                chess[newX][newY]=chess[x][y]+1

for i in answer:
    print(i)


#다른 풀이

from collections import deque
from sys import stdin
read = stdin.readline

dxy = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]


def bfs():
    q = deque()
    q.append(start)
    visit = [[0]*l for _ in range(l)]

    while q:
        x, y = q.popleft()
        if (x, y) == end:
            print(visit[x][y])
            return

        for dx, dy in dxy:
            nx, ny = x+dx, y+dy
            if not(0 <= nx < l and 0 <= ny < l):
                continue
            if visit[nx][ny] == 0:
                visit[nx][ny] = visit[x][y] + 1
                q.append((nx, ny))


t = int(read().strip())
for _ in range(t):
    l = int(read().strip())
    start = tuple(map(int, read().strip().split()))
    end = tuple(map(int, read().strip().split()))
    bfs()
