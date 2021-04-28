'''
풀이
lock의 구멍수 != key의 돌출부 수 False
lock의 구멍 사이 최대 길이 > key 돌출부 최대 길이 
lock 의 구멍 좌표 찾아놓기
key 후보들 4바퀴씩 돌리면서 lock 구멍좌표와 일치하는지 확인
key 후보들 중복제거 위해 비트마스킹 or set 사용
set을 사용하니 배열을 1차원으로 바꿈 =>[[1, 1, 1], [1, 1, 0], [1, 0, 1]] 111110101
'''
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = 	[[1, 1, 1], [1, 1, 0], [1, 0, 1]]

def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return ret

#후보좌표찾기
def get_holes(m):
    n = len(m)
    spot = []
    for i in range(n):
        for j in range(n):
            if m[i][j] == 0:
                spot.append(i*n+j)
    return spot

def get_keys(m):
    n = len(m)
    spot = []
    for i in range(n):
        for j in range(n):
            if m[i][j] == 1:
                spot.append(i*n+j)
    return spot

def get_keys_nums(m):
    n = len(m)
    num=0
    for i in range(n):
        for j in range(n):
            if m[i][j] == 1:
                num+=0
    return num

def move_up(m):
    n= len(m)
    ret = []
    ret = m[1:] + [0]*n
    return ret

def move_down(m):
    n= len(m)
    ret = []
    ret = [0]*n+ m[:-1]
    return ret

def move_left(m):
    n= len(m)
    ret = []
    for i in m:
        temp = i[1:] + [0]
        ret.append(temp)
    return ret

def move_right(m):
    n= len(m)
    ret = []
    for i in m:
        temp = [0]+i[:-1]
        ret.append(temp)
    return ret

def f(key,holes):
    visited = []
    need_visit = [key]
    while need_visit:
        #상하좌우 움직임으로 후보 찾기
        candi_key = []
        while True:
            up_key = move_up(key)
            keys = get_keys_nums(up_key)
            if keys != len(holes):
                break
            else:
                candi_key.append(up_key)
                key = up_key
        while True:
            down_key = move_down(key)
            keys = get_keys_nums(up_key)
            if keys != len(holes):
                break
            else:
                candi_key.append(down_key)
                key = down_key
        while True:
            left_key = move_left(key)
            keys = get_keys_nums(up_key)
            if keys != len(holes):
                break
            else:
                candi_key.append(left_key)
                key = left_key
        while True:
            right_key = move_right(key)
            keys = get_keys_nums(up_key)
            if keys != len(holes):
                break
            else:
                candi_key.append(right_key)
                key = right_key
        #90도씩 돌려서 후보찾기

def solution(key, lock):
    #후보 좌표 찾기
    holes = get_holes(lock)
    #구멍이 없을 때 성공
    if not holes:
        return True
    
    
    answer = True
    return answer