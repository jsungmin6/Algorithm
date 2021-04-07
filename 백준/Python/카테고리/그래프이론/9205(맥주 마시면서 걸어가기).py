'''
bfs로 이동할 다음 좌표 탐색
목적지에 무사히 도착하면 happy
실패하면 sad
인수로 남은 걸음 수를 넣어줌.
'''
import sys
from collections import deque
input = sys.stdin.readline


def bfs(sx,sy,n):
    q,visited=deque(),[]
    q.append([sx,sy,n])
    visited.append([sx,sy])
    while q:
        x,y,w = q.popleft()

        if x == end[0] and y == end[1]:
            print("happy")
            return
        
        for nx,ny in cu:
            if [nx,ny] not in visited:
                diff = abs(x-nx) + abs(y-ny)
                if w >= diff:
                    q.append([nx,ny,1000])
                    visited.append([nx,ny])
    print("sad")
    return

t = int(input())
for _ in range(t):
    n = int(input()) # 편의점 수
    start = list(map(int,input().split()))
    cu = [list(map(int,input().split())) for i in range(n)]
    end = list(map(int,input().split()))
    cu.append(end)
    bfs(start[0],start[1],1000)


