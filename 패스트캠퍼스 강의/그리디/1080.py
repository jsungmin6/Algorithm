# 저울

# 풀이 방법

'''
3*3 을 무조건 뒤집으니까 시작좌표와 끝좌표를 찾은 후 좌표를 돌면서 일치하면 패스하고 다르면 뒤집으면서 진행해 보고
끝까지 돌렸는데 행렬이 같지 않으면 -1 반환

'''
N, M = map(int, input().split())
Map = [list(input()) for i in range(N)]
result = [list(input()) for i in range(N)]

r = N-3
c = M-3


def reverse(i, j):
    for u in range(3):
        for v in range(3):
            if Map[i+u][j+v] == '1':
                Map[i+u][j+v] = '0'
            else:
                Map[i+u][j+v] = '1'


answer = 0
for i in range(r+1):
    for j in range(c+1):
        if Map[i][j] != result[i][j]:
            reverse(i, j)
            answer += 1

if Map == result:
    print(answer)
else:
    print(-1)
