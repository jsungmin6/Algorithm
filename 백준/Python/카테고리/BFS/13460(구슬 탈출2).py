'''
풀이
왼쪽, 오른쪽, 위, 아래로 이동했을 때 R과 B의 위치를 반환하는 함수를 작성
bfs로 몇 번 안에 R이 구멍으로 들어가는지 체크
B가 들어간다면 종료
10회가 넘어간다면 종료 후 -1 출력
'''
import sys
import bisect
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
mat = [list(input().rstrip()) for i in range(N)]
s_row,s_cul = [[] for i in range(N)],[[] for j in range(M)]
door,start_R,start_B=[],[],[]
for i in range(N):
    for j in range(M):
        if mat[i][j] == '#':
            s_row[i].append(j)
            s_cul[j].append(i)
        elif mat[i][j] == 'O':
            door = [i,j]
        elif mat[i][j] == 'R':
            start_R = [i,j]
        elif mat[i][j] == 'B':
            start_B = [i,j]

def mat_to_left(R,B):
    Rx,Ry = R
    Bx,By = B
    #R구슬 왼쪽에 가장 큰 #위치 찾기
    
    r_idx = bisect.bisect_left(s_row[Rx],Ry)
    b_idx = bisect.bisect_left(s_row[Bx],By)
    new_Ry = s_row[Rx][r_idx-1]+1
    new_By = s_row[Bx][b_idx-1]+1

    #구슬이 구멍으로 탈출하는 경우
    if Bx == door[0] and new_By <= door[1] < By:
        return 0
    if Rx == door[0] and new_Ry <= door[1] < Ry:
        return 1

    #같은 행에 있으면서 겹칠경우 위치 +1 처리
    if Rx == Bx and new_Ry == new_By:
        if Ry > By:
            new_Ry+=1
        else:
            new_By+=1

    #구슬 좌표 반환
    return [Rx,new_Ry],[Bx,new_By]

def mat_to_right(R,B):
    Rx,Ry = R
    Bx,By = B

    r_idx = bisect.bisect_left(s_row[Rx],Ry)
    b_idx = bisect.bisect_left(s_row[Bx],By)
    new_Ry = s_row[Rx][r_idx]-1
    new_By = s_row[Bx][b_idx]-1

    #구슬이 구멍으로 탈출하는 경우
    if Bx == door[0] and By < door[1] <= new_By:
        return 0
    if Rx == door[0] and Ry < door[1] <= new_Ry:
        return 1

    #같은 행에 있으면서 겹칠경우 위치 +1 처리
    if Rx == Bx and new_Ry == new_By:
        if Ry > By:
            new_By-=1
        else:
            new_Ry-=1
    
    #구슬 좌표 반환
    return [Rx,new_Ry],[Bx,new_By]

def mat_to_up(R,B):
    Rx,Ry = R
    Bx,By = B

    r_idx = bisect.bisect_left(s_cul[Ry],Rx)
    b_idx = bisect.bisect_left(s_cul[By],Bx)
    new_Rx = s_cul[Ry][r_idx-1]+1
    new_Bx = s_cul[By][b_idx-1]+1

    #구슬이 구멍으로 탈출하는 경우
    if By == door[1] and new_Bx <= door[0] < Bx:
        return 0
    if Ry == door[1] and new_Rx <= door[0] < Rx:
        return 1

    #같은 행에 있으면서 겹칠경우 위치 +1 처리
    if Ry == By and new_Rx == new_Bx:
        if Rx > Bx:
            new_Rx+=1
        else:
            new_Bx+=1
    
    #구슬 좌표 반환
    return [new_Rx,Ry],[new_Bx,By]

def mat_to_down(R,B):
    Rx,Ry = R
    Bx,By = B

    r_idx = bisect.bisect_left(s_cul[Ry],Rx)
    b_idx = bisect.bisect_left(s_cul[By],Bx)
    new_Rx = s_cul[Ry][r_idx]-1
    new_Bx = s_cul[By][b_idx]-1

    #구슬이 구멍으로 탈출하는 경우
    if By == door[1] and Bx < door[0] <= new_Bx:
        return 0
    if Ry == door[1] and Rx < door[0] <= new_Rx:
        return 1

    #같은 행에 있으면서 겹칠경우 위치 +1 처리
    if Ry == By and new_Rx == new_Bx:
        if Rx > Bx:
            new_Bx-=1
        else:
            new_Rx-=1
    
    #구슬 좌표 반환
    return [new_Rx,Ry],[new_Bx,By]

def bfs(R,B):
    visited=[]
    visited.append([R[0],R[1],B[0],B[1]])
    q = deque([[R,B]])
    cnt = 0
    while q:
        q_size = len(q)
        cnt+=1
        if cnt > 10:
            return -1
        for i in range(q_size):
            r,b = q.popleft()
            temp = []
            left_result = mat_to_left(r,b)
            if left_result == 1:
                return cnt
            if left_result != 0:
                temp.append(left_result)

            right_result = mat_to_right(r,b)
            if right_result == 1:
                return cnt
            if right_result != 0:
                temp.append(right_result)

            up_result = mat_to_up(r,b)
            if up_result == 1:
                return cnt
            if up_result != 0:
                temp.append(up_result)

            down_result = mat_to_down(r,b)
            if down_result == 1:
                return cnt
            if down_result != 0:
                temp.append(down_result)

            for result_R,result_B in temp:
                v = result_R+result_B
                if v in visited:
                    continue
                visited.append(v)
                q.append([result_R,result_B])
    return -1

print(bfs(start_R,start_B))