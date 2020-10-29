# 2048 (Easy)

# 풀이 방법

'''
left right up down 함수를 만든다.
그리고 5번 이니까 경우의 수를 만든다. 4*4*4*4*4 = 2^10 = 1024개의 경우를 모두 구하고 최댓값을 구한다.

left()
한 행의 0을 제외하고 수를 모두 뽑는다.
인접하는 숫자가 같다면 더하고 빈자리에 0을 넣음 2 2 2 2 -> 4 0 4 0
여기서 다시 0을제거한 후 오른쪽에 배열 크기만큼 0을 채워 줌 4 0 4 0 -> 4 4 0 0
두번 반복하진 않으니 여기서 종료다. 

이렇게 하려고 했으나 강사는
4방향을 모두 하는 것보다 이런 문제에선 map을 90로 돌려가면서 한방향으로 로직을 구성하는게 좋다고 한다.
map을 90도로 돌리는 방법은 선형대수학이나 다른곳에서 따로 배우지 않았으면 외우자.

'''
# # # # # # # # # # # # # # # # # # # # # 내 풀이
import sys
from copy import deepcopy
input = sys.stdin.readline
N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]


def convert(row, N):
    temp = [i for i in row if i]
    for i in range(1, len(temp)):
        if temp[i-1] == temp[i]:
            temp[i-1] = temp[i-1]*2
            temp[i] = 0

    temp = [i for i in temp if i]
    return temp + [0]*(N-len(temp))


def rotate90(N, M):
    NB = deepcopy(M)
    for i in range(N):
        for j in range(N):
            NB[j][N-i-1] = M[i][j]
    return NB


def solution(N, M, count):  # 최댓값을 구해야 함.
    ret = max([max(i) for i in M])

    if count == 0:
        return ret

    for _ in range(4):
        new_Map = [convert(r, N) for r in M]  # 덧셈 결과

        if new_Map != M:  # 덧셈 결과와 기존 Map의 차이가 있으면 한번더 진행
            ret = max(ret, solution(N, new_Map, count-1))

        M = rotate90(N, M)  # 덧셈 결과와 기존 MAp의 차이가 없으면 기존Map을 90도 돌려줘서 진행.

    return ret


print(solution(N, Map, 5))
