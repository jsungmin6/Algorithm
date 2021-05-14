'''

풀이

최단거리를 활용한 시뮬레이션

1.손님찾기
택시의 현재위치 남은 손님의 위치자표를 토대로 가장 택시와 가까운 손님을 고른다.
- bfs를 통해 최단거리에 위치한 모든 손님리스트를 구한다.
- 손님리스트를 행 오름차순, 열 오름차순으로 정렬 후 0번째 인덱스의 손님을 고른다.

2.이동 가능 여부 체크
손님위치과 택시 dfs 계산 + 손님위치와 목적지 dfs 계산한게 현재 연료 [이하]면 드라이브 가능
이동이 가능하다면
- 택시 현재 위치를 손님 도착위치로 바꿔줌
- 손님을 후보에서 제거
- 연료 갱신
이동이 불가능 하다면
- -1 리턴하고 종료

3.남은 손님 리스트가 없을때까지 진행하고 연료 리턴

'''
from collections import deque
import sys
input = sys.stdin.readline

N,M,gas = map(int,input().split())
mat = [list(map(int,input().split())) for i in range(N)]
start = list(map(int,input().split()))
guests = [list(map(int,input().split())) for i in range(M)]
derive_cnt = 0

guests_start,guests_end = [],[]
dx,dy = [0,0,1,-1],[-1,1,0,0]

for i,geust in enumerate(guests):
    guests_start.append([geust[0]-1,geust[1]-1])
    guests_end.append([geust[2]-1,geust[3]-1])

    mat[geust[0]-1][geust[1]-1] = (i+1)*(-1) # 손님 위치와 인덱스 표시

def is_in_mat(x,y):
    if x<0 or x==N or y<0 or y==N:
        return False
    return True

def find_candi(cx,cy):

    visited = [[0 for i in range(N)] for j in range(N)]
    q = deque([[cx,cy]])
    ch = False
    candi_li = []

    #자기위치라면
    if mat[cx][cy] < 0:
        return [[cx,cy,mat[cx][cy]]]

    while q:
        # print("q : ",q)
        q_size = len(q)

        if ch:
            return candi_li

        for _ in range(q_size):
            tx,ty = q.popleft()

            for i in range(4):
                nx,ny = dx[i]+tx,dy[i]+ty

                if is_in_mat(nx,ny) and not visited[nx][ny] and mat[nx][ny] != 1:

                    if mat[nx][ny] < 0:
                        ch=True
                        candi_li.append([nx,ny,mat[nx][ny]])
                    visited[nx][ny] = 1
                    q.append([nx,ny])

    # print("candi_li : ",candi_li)
    return candi_li

def find_guest(t):
    cx,cy = t[0],t[1]

    gs = find_candi(cx,cy)


    if not gs:
        return False
    elif len(gs) == 1:
        return gs[0]
    else:
        gs.sort()
        return gs[0]

def dist(sx,sy,ex,ey):

    visited = [[0 for i in range(N)] for j in range(N)]
    visited[sx][sy] = 1
    q = deque([[sx,sy]])
    d = 0
    ch=True

    while q:
        q_size = len(q)
        for _ in range(q_size):
            tx,ty = q.popleft()

            if tx == ex and ty == ey:
                # print("거리 : ",d)
                return d

            for i in range(4):
                
                nx,ny = dx[i]+tx,dy[i]+ty

                if is_in_mat(nx,ny) and not visited[nx][ny] and mat[nx][ny] != 1:
                    visited[nx][ny] = 1
                    q.append([nx,ny])
        d+=1

    if ch:#경로가 없는 경우
        return "NOWAY"
    return d




def drive(tx,ty,gx,gy,gi):
    global gas
    #도착을 못한다면 false
    tx_to_gs = dist(tx,ty,gx,gy)
    # print("tx_to_gs : ",tx_to_gs)
    # print("시작,끝 : ",gx,gy,guests_end[gi][0],guests_end[gi][1])
    gs_to_dest = dist(gx,gy,guests_end[gi][0],guests_end[gi][1])
    # print("gs_to_dest : ",gs_to_dest)

    if tx_to_gs == "NOWAY" or gs_to_dest == "NOWAY":
        return False

    if gas >= tx_to_gs+gs_to_dest:
        gas = gas-tx_to_gs+gs_to_dest
        return True
    else:
        return False

cul_taxi = [start[0]-1,start[1]-1]

while True:
    g = find_guest(cul_taxi)
    
    # for i in mat:
    #     print(i)
    # print()

    # print("g : ",g)
    # print("gas : ",gas)

    if not g:
        if derive_cnt < M:
            print(-1)
        else:
            print(gas)
        break

    gx,gy,gi = g[0],g[1],(g[2]+1)*(-1)

    if not drive(cul_taxi[0],cul_taxi[1],gx,gy,gi):
        print(-1)
        break
    else:
        mat[gx][gy] = 0
        cul_taxi[0] = guests_end[gi][0]
        cul_taxi[1] = guests_end[gi][1]
    
    derive_cnt+=1
    
    