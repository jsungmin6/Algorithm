#복제 로봇

#풀이 방법

'''
1.로봇 출발위치와 key의 위치를 저장해 dfs 에 활용
2.저장한 각각의 좌표들을 모두 dfs 돌려 좌표간 가중치를 찾아 graph를 만든다.
3.크루스칼 알고리즘 발동
'''

# # # # # # # # # # # # # # # # # # # # 내 풀이
import sys
from collections import deque
input=sys.stdin.readline

def find(n):
    if p[n]==n:
        return n;
    p[n]=find(p[n])
    return p[n]


def union(a,b):
    a=find(a)
    b=find(b)
    if a==b:
        return
    if level[a]<level[b]:
        p[a]=b
    elif level[a] >level[a]:
        p[b]=a;
    else:
        p[b]=a
        level[a]+=1

def in_maze(x,y):
    if 0<=x<N and 0<=y<N:
        return True
    else:
        return False

#S,K 좌표목록들을 하나씩 bfs 돌려주고, 그 좌표가 다른 S,K 를 만날 때마다 graph 에 추가해준다.
#중복은 최대한 피해준다.
#만약에 모두 만나지 못하는 경우를 isAccess 를 통해 걸러준다.
def bfs(here):
    isAccess=0
    visited=[[0 for j in range(N)] for i in range(N)]
    need_visited=deque([key_point[here]])
    while need_visited:
        node = need_visited.popleft()
        x=node[0]
        y=node[1]

        for i in range(4):
            new_x=x+dx[i]
            new_y=y+dy[i]

            if in_maze(new_x,new_y) and visited[new_x][new_y]==0 and maze[new_x][new_y]!="1":
                visited[new_x][new_y] = visited[x][y]+1
                need_visited.append([new_x,new_y])
                if maze[new_x][new_y]=="S" or maze[new_x][new_y]=="K":
                    mst_list.append([visited[new_x][new_y],num[key_point[here][0]][key_point[here][1]],num[new_x][new_y]])
                    isAccess+=1
    if isAccess == M+1:
        return True
    else:
        return False


N,M=map(int,input().split())
maze=[]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
key_point=[]
mst_list=[]
level=[0]*5000
p=[i for i in range(5000)]


for _ in range(N):
    maze.append(list(input())[:-1])

#nodeNum 만들어 인덱스 값으로 활용.
#S,K좌표 찾아서 key_point에 넣어 줌.
nodeNum=0
num=[[0 for j in range(N)] for i in range(N)]
for i in range(N):
    for j in range(N):
        if maze[i][j]=='S' or maze[i][j] == 'K':
            key_point.append([i,j])
        num[i][j]=nodeNum
        nodeNum+=1

#bfs 에 좌표 하나씩 넣어줌. false가 나올시 -1 리턴 하고 끝
for i in range(len(key_point)):
    if not bfs(i):
        print(-1)
        exit(0)


mst_list.sort()
sum_dist=0
cnt=0

for i in range(len(mst_list)):
    dist,a,b=mst_list[i]
    if find(a) != find(b):
        union(a,b)
        sum_dist+=dist;
        cnt+=1
    if cnt == M:
        break

print(sum_dist)
