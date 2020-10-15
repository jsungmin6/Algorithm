#백조의 호수

#풀이 방법

'''
L좌표를 저장하고 '.'으로만듬
'.'좌표를 union해서 하나의 덩어리로 만듬
얼음 녹이다가 find(L1좌표) = find(L2좌표) 일때 연결 된 것.

1.bfs 통해 merge 진행
2.find로 같은곳에 있는지 검사
3.bfs 통해 물 범위 확장
4.반복

==>계속 시간초과
'''

# # # # # # # # # # # # # # # # # # # # # 내 풀이
dx=[0,0,1,-1]
dy=[1,-1,0,0]

#union find를 2차원으로 했음
def find(n:list):
    x=n[0]
    y=n[1]
    if rake[x][y]==[x,y]:
        return n;
    rake[x][y] = find(rake[x][y]);
    return rake[x][y]

def merge(a:list,b:list):
    a=find(a);
    b=find(b);
    if(a==b):
        return
    rake[b[0]][b[1]]=a;

#좌표가 범위안에 있는지
def inRake(x,y):
    if 0 <= x and x < R and 0 <= y and y < C:
        return True;
    return False;

#bfs로 merge진행
def bfs_merge():
    while q_rake: # q_rake 에 '.'들 좌표 넣어줌
        node=q_rake.popleft()
        if node in visited:
            continue
        else:
            visited.append(node)

            #현재좌표
            current_x=node[0]
            current_y=node[1]

            #물들을 q_melt에 넣어줌
            q_melt.append([current_x,current_y])
            for i in range(4):
                #다음좌표
                new_x=current_x+dx[i]
                new_y=current_y+dy[i]

                #범위안에 좌표가 'X'가 아니고 다음좌표와 현재좌표가 같지 않으면 merge 진행
                if(inRake(new_x,new_y) and rake[new_x][new_y]!=-1 and rake[current_x][current_y] != rake[new_x][new_y]):
                    merge(node,[new_x,new_y])

def bfs_water():
    while q_melt:
        node=q_melt.popleft()
        current_x=node[0]
        current_y=node[1]

        for i in range(4):
            new_x=current_x+dx[i]
            new_y=current_y+dy[i]

            #범위안에 다음좌표가 'X' 이면 현재좌표를 다음좌표에 넣어 주고 q_rake에 다음좌표를 넣어줘서 merge할 수 있도록 함
            if(inRake(new_x,new_y) and rake[new_x][new_y]==-1):
                rake[new_x][new_y]=rake[current_x][current_y]
                q_rake.append([new_x,new_y])

import sys
from collections import deque
input = sys.stdin.readline
R,C= map(int,input().split())
rake=[]
visited=[]
q_melt=deque()
q_rake=deque()
ans=0

for _ in range(R):
    rake.append(list(input().split()[0]))

duck_point=[]

#좌표로 변환
for i in range(R):
    for j in range(C):
        if rake[i][j] == '.':
            rake[i][j]=[i,j]
            q_rake.append([i,j])
        elif rake[i][j] == 'L':
            duck_point.append([i,j])
            rake[i][j]=[i,j]
            q_rake.append([i,j])
        else:
            rake[i][j]=-1


while True:
    #union find로 덩어리로 만들어줌
    bfs_merge()

    #오리좌표의 대가리들이 일치하는지 검사
    if find(duck_point[0]) == find(duck_point[1]):
        print(ans)
        break;

    #얼음 녹아서 물 확장
    bfs_water()
    ans+=1
