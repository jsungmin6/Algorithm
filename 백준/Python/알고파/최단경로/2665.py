# 미로만들기

# 풀이 과정
'''
같은 흰색이면 가중치가 0 검은곳으로 갈땐 가중치가 1 로 해서 다익스트라로 가중치를 최소값을 구한다.
graph를 만들때 지점을 좌표로 해도 될까?
'''

import sys
import collections
import heapq
input = sys.stdin.readline

n=int(input())

M = [list(map(int,list(input().rstrip()))) for i in range(n)]

for i in range(n):
    for j in range(n):
        if M[i][j] == 1:
            M[i][j] = 0
        else :
            M[i][j] = 1

graph = collections.defaultdict(list)

dx=[1,-1,0,0]
dy=[0,0,-1,1]

def in_map(x,y):
    if x<0 or y<0 or x==n or y==n:
        return False
    return True

for i in range(n):
    for j in range(n):
        for k in range(4):
            new_x = i+dx[k]
            new_y = j+dy[k]
            if not in_map(new_x,new_y):
                continue
            graph[(i,j)].append(((new_x,new_y),M[new_x][new_y]))

dist = collections.defaultdict(int)
Q=[(0,(0,0))]

while Q:
    weight, node = heapq.heappop(Q)
    if node in dist:
        continue
    dist[node] = weight
    for i in graph[node]:
        if i[0] in dist:
            continue
        alt = i[1]+weight
        heapq.heappush(Q,(alt,i[0]))

print(dist[(n-1,n-1)])
        
#########################다른풀이 (깔끔)
'''
graph를 구지 안만들고 상하좌우 자표에서 범위 안에 있는 좌표만 큐에 넣어주는 식
'''
from sys import*
from heapq import*
input = lambda : stdin.readline().strip()

n=int(input())
arr=[list(map(int,input()))for _ in range(n)]
pq=[]
INF=98765321
dist=[[INF]*n for _ in range(n)]
heappush(pq,(0,0,0))
dist[0][0]=0
visit=[[-1]*n for _ in range(n)]
visit[0][0]=0
while pq:
    d,x,y=heappop(pq)
    if x==n-1 and y==n-1:
        break
    for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx , ny = x+dx , y+dy
        if nx<0 or ny<0 or nx>n-1 or ny>n-1 :continue
        nd=(1-arr[nx][ny])+d
        if dist[nx][ny] > nd :
            dist[nx][ny]=nd
            heappush(pq,(nd,nx,ny))

print(dist[n-1][n-1])
