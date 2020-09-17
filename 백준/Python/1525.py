#0의 위치 찾기
#0 동서남북 위치 바꾸기 bfs 로 최소거리 구하기
#check 함수 만들어 순서대로 되어있는지 계속 확인
from collections import deque

data=list()
for _ in range(3):
    data.append(list(map(int,input().split())))

for i in range(len(data)):
    if 0 in data[i]:
        for j in range(len(data[i])):
            if 0==data[i][j]:
                x=i;
                y=j

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def check(array):
    if array[0]==[1,2,3] and array[1]==[4,5,6] and array[2]==[7,8,0]:
        return True
    else:
        False

visited=[[0]*3 for i in range(3)]

def bfs(x,y):
    need_visit=deque([[x,y]])
    count=0
    a=x
    b=y
    while need_visit:

        node=need_visit.popleft()
        x=node[0]
        y=node[1]
        visited[x][y]=1

        for i in data:
            print(i)
        data[a][b]=data[x][y]
        data[x][y]=0
        a,b=x,y

        count+=1
        print()

        for i in data:
            print(i)

        if check(data):
            return count


        for i in range(4):
            new_x=x+dx[i]
            new_y=y+dy[i]
            if new_x>=0 and new_y>=0 and new_x<=2 and new_y<=2 and visited[new_x][new_y]==0:
                need_visit.appendleft([new_x,new_y])
        print(need_visit)

bfs(x,y)
