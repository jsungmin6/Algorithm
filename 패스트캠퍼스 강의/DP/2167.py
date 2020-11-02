# #############################DP 사용

'''
DP를 이용해 누적합 배열을 구해준다.
'''

N, M = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]
DP = [[0 for i in range(M+1)] for j in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        DP[i][j] = DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1] + A[i-1][j-1]


K = int(input())

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    print(DP[x2][y2] - DP[x2][y1-1] - DP[x1-1][y2] + DP[x1-1][y1-1])