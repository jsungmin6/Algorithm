'''
풀이
시키는 대로 구현

Map 초기화
visited 초기화

1.청소하기
visited 등록

2.보든방향의 왼쪽 방향에 공간 있는지 체크 (시계 반대방향 : 북 서 남 동 북 서 남 동 순으로 체크)
0 1 2 3 이니 -1 해준 방향이 있는지 체크

3.이동할 곳이 있다면 이동 후 1,2반복

4.4방향 모두 청소 했다면 방향 유지한체 후진

5.후진할 곳이 벽이라면 종료

'''
def check_in(new_r,new_c):
    if new_r == N or new_r < 0  or new_c < 0 or new_c == M:
        return False
    return True


def check_visited(new_r,new_c):
    if not check_in(new_r,new_c):
        return False
    if visited[new_r][new_c]:
        return False
    if Map[new_r][new_c] == 1:
        return False
    return True

def check_finish(new_r,new_c):
    if not check_in(new_r,new_c):
        return True
    if Map[new_r][new_c] == 1:
        return True
    return False

def back_point(r,c,new_d):
    if new_d == 0:
        new_r = r+1
        new_c = c
    elif new_d == 1:
        new_r = r
        new_c = c-1
    elif new_d == 2:
        new_r = r-1
        new_c = c
    elif new_d == 3:
        new_r = r
        new_c = c+1
    
    return [new_r,new_c]

N,M = map(int,input().split())
r,c,d = map(int,input().split())

Map = []
for i in range(N):
    row = list(map(int,input().split()))
    Map.append(row)

visited = [[False for i in range(M)] for j in range(N)]
cnt=0

while True:

    #청소하기
    # print('r,c,d:',r,c,d)
    if not visited[r][c]:
        cnt+=1
    visited[r][c] = True

    #보든방향의 왼쪽 방향에 공간 있는지 체크 (시계 반대방향 : 서3 남2 동1 북0 순으로 체크)
    ch_move=False
    for k in range(1,5):
        new_d = d-k
        if new_d<0:
            new_d = 4+new_d

        if new_d == 0:
            new_r = r-1
            new_c = c
        elif new_d == 1:
            new_r = r
            new_c = c+1
        elif new_d == 2:
            new_r = r+1
            new_c = c
        elif new_d == 3:
            new_r = r
            new_c = c-1
        # print("new_r,new_c",new_r,new_c)
        #시계방향으로 청소 안 한 곳 있나 체크
        if check_visited(new_r,new_c):
            
            ch_move=True

            #이동
            r,c,d = new_r,new_c,new_d
            break;

    # print("ch_move : ",ch_move)
    #이동 했다면
    if ch_move:
        continue
    
    #청소할 곳이 없고 뒤가 벽이면
    back_r,back_c = back_point(r,c,d)
    # print('back_r,back_c :',back_r,back_c)
    if not ch_move and check_finish(back_r,back_c):
        break
    
    #청소할 곳이 없고 뒤가 벽이 아니면
    if not ch_move and not check_finish(back_r,back_c):
        r,c= back_r,back_c
        continue
        
print(cnt)