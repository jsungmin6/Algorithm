#구간 합 구하기 5

#풀이 방법

'''
for 문 행방향 열발향으로 두번 누적합 구한 후 좌표로 계산
'''

# # # # # # # # # # # # # # # # # # # # # 내 풀이
import sys
input=sys.stdin.readline
N,M=map(int,input().split())

#매트릭스 위, 왼쪽에 0을 붙여줌. -> 인덱스 벗어나는 오류 해결 위함
matrix=[[0]*N]
for _ in range(N):
    matrix.append(list(map(int,input().split())))

for i in range(len(matrix)):
    matrix[i].insert(0,0)

#누적합 배열 만들기
for i in range(len(matrix)):
    for j in range(len(matrix)-1):
        matrix[i][j+1]+=matrix[i][j]

for i in range(len(matrix)):
    for j in range(len(matrix)-1):
        matrix[j+1][i]+=matrix[j][i]

for _ in range(M):
    x1,y1,x2,y2=map(int,input().split())
    print(matrix[x2][y2]+matrix[x1-1][y1-1]-matrix[x2][y1-1]-matrix[x1-1][y2])
