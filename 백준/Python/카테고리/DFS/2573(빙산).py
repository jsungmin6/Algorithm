'''
풀이
dfs 컴퍼넌트 수를 세는 것으로 빙산의 수가 2 이상이 되는지 체크
1년이 지날때의 map을 다시 만드는 함수
두개를 반복 함.
다 0이 되면 0을 출력
'''
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

dx=[0,0,1,-1]
dy=[1,-1,0,0]
def ch_in(x,y):
    if x <0  or y<0 or x == N or y == M:
        return False
    return True

def melt(Map):
    ch_all_melt=True
    temp=[[0 for i in range(M)] for j in range(N)]
    for i in range(N):
        for j in range(M):
            if Map[i][j] == 0:
                continue
            else:
                cnt=0
                for k in range(4):
                    new_x=i+dx[k]
                    new_y=j+dy[k]

                    if not ch_in(new_x,new_y):
                        continue
                    if Map[new_x][new_y] != 0:
                        continue
                    cnt+=1
                temp[i][j] = cnt

    for i in range(N):
        for j in range(M):
            if Map[i][j] == 0:
                continue
            else:
                Map[i][j] = max(0,Map[i][j]-temp[i][j])
                if Map[i][j] > 0 :
                    ch_all_melt = False
    return ch_all_melt

def iceberg(Map):
    visited = [[False for i in range(M)] for j in range(N)]
    iceNum=0
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and Map[i][j] != 0:
                dfs(i,j,visited)
                iceNum+=1
    return iceNum

def dfs(i,j,visited):
    visited[i][j] = True
    for k in range(4):
        new_x = i+dx[k]
        new_y = j+dy[k]

        if not ch_in(new_x,new_y):
            continue
        if visited[new_x][new_y]:
            continue
        if Map[new_x][new_y] == 0:
            continue
        
        

        dfs(new_x,new_y,visited)

N,M = map(int,input().split())
Map = []
for _ in range(N):
    Map.append(list(map(int,input().split())))

iceNum = 1
time = 0
while iceNum < 2:
    all_melt = melt(Map)
    time+=1
    if all_melt:
        time = 0
        break
    # for i in Map:
    #     print(i)
    # print()
    iceNum = iceberg(Map)
    # print("iceNum : ",iceNum)

print(time)