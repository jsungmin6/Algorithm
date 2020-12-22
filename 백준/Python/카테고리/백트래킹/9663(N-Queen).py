'''
퀸이 서로 공격할 수 없도록 하는 경우의 수
파이썬으로 풀기 힘든 문제
백트래킹은 파이썬이 힘들다.
'''
N = int(input())

Map = []
cnt = 0


def check(Map, r, c):
    # 열s
    for i in range(r):
        if Map[i][c] == 1:
            # print('열F')
            return False
    # 좌 대각선
    for i in range(1, r+1):
        if r-i < 0 or c-i < 0:
            break
        if Map[r-i][c-i] == 1:
            # print('대F')
            return False
    # 우 대각선
    for i in range(1, r+1):
        if r-i < 0 or c+i == N:
            break
        if Map[r-i][c+i] == 1:
            # print('대F')
            return False
    # print('T')
    return True


def back(Map, cur_r):
    global cnt
    if cur_r == N:
        cnt += 1
        # for m in Map:
        #     print(m)
        # print('이거 추가')

        return

    for i in range(N):
        cur_c = i
        temp = [0]*N
        temp[cur_c] = 1
        Map.append(temp)

        # for m in Map:
        #     print(m)

        if not check(Map, cur_r, cur_c):
            Map.pop()
            continue

        back(Map, cur_r+1)
        Map.pop()


back(Map, 0)
print(cnt)


#좋은 코드
#내 윗줄에 나와 겹치는 라인에 퀸이 있는가?
def adjacent(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True
        
        
#한줄씩 재귀하며 DFS를 실행
def dfs(x):
    global result
    
    if x == N:
        result += 1

    else:
        for i in range(N):
            row[x] = i
            if adjacent(x):
                dfs(x + 1)

N = int(input())
row = [0] * N
result = 0
dfs(0)
print(result)