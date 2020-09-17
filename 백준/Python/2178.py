from collections import deque

N,M = map(int,input().split())

arr = []

#테스트 필요
for i in range(N):
    arr.append(list(map(int,list(input()))))

#남 동 북 서
dx=[0,1,0,-1]
dy=[1,0,-1,0]

temp=[[False]*M for _ in range(N)]


def bfs():
    need_visit=deque([[0,0]])
    while need_visit:
        k=need_visit.popleft()
        x=k[0]
        y=k[1]
        temp[x][y]=True

        for i in range(4):
            if x+dx[i]>=0 and x+dx[i]<N and y+dy[i]>=0 and y+dy[i]<M and temp[x+dx[i]][y+dy[i]]==False:
                if arr[x+dx[i]][y+dy[i]]==1:
                    arr[x+dx[i]][y+dy[i]]+=arr[x][y]
                    need_visit.append([x+dx[i],y+dy[i]])

    return arr[N-1][M-1]

print(bfs())
