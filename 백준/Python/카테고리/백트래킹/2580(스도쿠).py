from copy import deepcopy
import sys
input = sys.stdin.readline


Map = [list(map(int, input().split())) for i in range(9)]
emp = []
answer = []
for i in range(9):
    for j in range(9):
        if Map[i][j] == 0:
            emp.append([i, j])


def check(emp, i):
    x, y = emp
    # 행
    if i in Map[x]:
        return False
    # 열
    for j in range(9):
        if Map[j][y] == i:
            return False
    # 범위
    for j in range((x//3)*3, (x//3)*4):
        for k in range((y//3)*3, (y//3)*4):
            if Map[j][j] == i:
                return False

    return True


result = []


def back(k):  # k번째 빈칸
    global result
    if k == len(emp):
        result = deepcopy(answer)
        return answer

    for i in range(1, 10):
        # k번째 빈칸에 i를 넣음
        if not check(emp[k], i):
            continue

        x, y = emp[k]
        Map[x][y] = i
        answer.append(i)

        back(k+1)

        Map[x][y] = 0
        answer.pop()


back(0)

for i, emp in enumerate(emp):
    x, y = emp
    Map[x][y] = result[i]

for r in Map:
    for i in r:
        print(i, end=' ')
    print()


# 모든 수를 넣지 않고 후보를 먼저 뽑아 걸러주는 방식으로 시간을 줄인듯
sudoku = [list(map(int, input().split())) for _ in range(9)]
# 해결해야될 칸만 받음
zeros = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]


def is_promising(i, j):
    promising = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 행열 검사
    for k in range(9):
        if sudoku[i][k] in promising:
            promising.remove(sudoku[i][k])
        if sudoku[k][j] in promising:
            promising.remove(sudoku[k][j])

    # 3*3 박스 검사
    i //= 3
    j //= 3
    for p in range(i*3, (i+1)*3):
        for q in range(j*3, (j+1)*3):
            if sudoku[p][q] in promising:
                promising.remove(sudoku[p][q])

    return promising


flag = False  # 답이 출력되었는가?


def dfs(x):
    global flag

    if flag:  # 이미 답이 출력된 경우
        return

    if x == len(zeros):  # 마지막 0까지 다 채웠을 경우
        for row in sudoku:
            print(*row)
        flag = True  # 답 출력
        return

    else:
        (i, j) = zeros[x]
        promising = is_promising(i, j)  # 유망한 숫자들을 받음

        for num in promising:
            sudoku[i][j] = num  # 유망한 숫자 중 하나를 넣어줌
            dfs(x + 1)  # 다음 0으로 넘어감
            sudoku[i][j] = 0  # 초기화 (정답이 없을 경우를 대비)


dfs(0)
