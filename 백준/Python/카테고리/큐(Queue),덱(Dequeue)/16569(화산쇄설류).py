'''
풀이
자신이 갈수 있는 위치 영역 bfs 로 확장 및 기록(시간, 좌표)
화산이 덮이는 영역 bfs로 확장
자신이 갈 수 있는 위치가 없을 경우 종료
최고 높이 좌표의 시간 출력

1.화산 확장
2.자신 범위 확장
3.반복

'''
import sys
from collections import deque
input = sys.stdin.readline

M,N,V = map(int,input().split())
X,Y = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(M)]
visited_v = [[0 for i in range(N)] for j in range(M)] # 화산쇄설문 방문
visited_h = [[0 for i in range(N)] for j in range(M)] # 사람이 방문
spot = [[] for i in range(500)] # 화산위치, 시간
v_spot = [[0 for i in range(N)] for j in range(M)] #화산위치
visited_h[X-1][Y-1] = 1 # 사람 처음 위치 방문 처리
for i in range(V):
    xi,yi,ti = map(int,input().split())
    spot[ti].append([xi-1,yi-1])
    v_spot[xi-1][yi-1] = 1
dx,dy = [0,0,-1,1],[-1,1,0,0]
answer = [mat[X-1][Y-1],0] # 처음 위치 초기화

#범위 안에 있는지 확인
def check_in_mat(x,y):
    if x<0 or y<0 or x > M-1 or y > N-1:
        return False
    return True

#화산 확장
def bfs_v(q_list):
    q = deque(q_list)
    next_q=[]
    while q:
        x,y = q.popleft()
        for i in range(4):
            new_x, new_y = x+dx[i],y+dy[i]

            if not check_in_mat(new_x,new_y):
                continue
            if visited_v[new_x][new_y]:
                continue
            visited_v[new_x][new_y]=1
            next_q.append([new_x,new_y])
    return next_q

#인간 확장
def bfs_h(q_list):
    q = deque(q_list)
    next_q=[]
    while q:
        x,y = q.popleft()
        for i in range(4):
            new_x, new_y = x+dx[i],y+dy[i]

            if not check_in_mat(new_x,new_y):
                continue
            if visited_h[new_x][new_y]:
                continue
            if visited_v[new_x][new_y]:
                continue
            if v_spot[new_x][new_y]:
                continue
            visited_h[new_x][new_y] = visited_h[x][y]+1


            if answer[0] < mat[new_x][new_y]:
                answer[0] = mat[new_x][new_y]
                answer[1] = visited_h[new_x][new_y]-1
            
            next_q.append([new_x,new_y])
    return next_q

t = 0
v_list=[]
h_list=[[X-1,Y-1]]
while True:
    #시간에 해당하는 화산이 있다면 화산 리스트에 추가
    if spot[t]:
        for x,y in spot[t]:
            visited_v[x][y] = 1
            v_list.append([x,y])
    
    #화산이 존재한다면 화산 확장 진행 하고 화산 리스트 갱신
    if v_list:
        next_v_list = bfs_v(v_list)
        v_list = next_v_list
    
    #사람이 이동할 수 있는 범위 확장
    if h_list:
        next_h_list = bfs_h(h_list)
        h_list = next_h_list
    
    if not h_list:
        break;

    #시간 진행
    t+=1

print(*answer)
