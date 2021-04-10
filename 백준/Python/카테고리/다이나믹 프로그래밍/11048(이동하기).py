'''
풀이
방문했던곳을 경로가 달라졌을 때 다시 방문하며 결과값이 달라질 수 있다. 즉 전에 값이 다음 값에 영향을 끼친다.

dp[i][j] = max(dp[i-1][j],dp[i][j-1]) + mat[i][j] 시간초과

바텀업 방식으로 풀이

'''


N,M = map(int,input().split())
mat = [list(map(int,input().split())) for i in range(N)]
dp = [[0 for i in range(M+1)] for j in range(N+1)]


for i in range(1,N+1):
    for j in range(1,M+1):
        dp[i][j] = max(dp[i-1][j],dp[i][j-1]) + mat[i-1][j-1]

print(dp[N][M])



### 91퍼 시간초과
# import sys
# input = sys.stdin.readline
# sys.setrecursionlimit(2000)

# N,M = map(int,input().split())
# mat = [list(map(int,input().split())) for i in range(N)]
# start = (0,0)
# end = (N-1,M-1)

# dp = [[0 for i in range(M)] for i in range(N)]

# def sol(x,y):
#     if x == 0 and y == 0:
#         return mat[0][0]
#     if dp[x][y] != 0:
#         return dp[x][y]
#     if x<0 or y<0 or x==N or y == M:
#         return -1

#     dp[x][y] = max(sol(x-1,y),sol(x,y-1)) + mat[x][y]

#     return dp[x][y]

# answer = sol(N-1,M-1)

# print(answer)



# 탑 다운
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N,M = map(int,input().split())
mat = [list(map(int,input().split())) for i in range(N)]
start = (0,0)
end = (N-1,M-1)

dp = [[-1 for i in range(M)] for i in range(N)]

def sol(x,y):
    if x<0 or y<0:
        return -1
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = max(sol(x-1,y),sol(x,y-1)) + mat[x][y]

    return dp[x][y]

dp[0][0] = mat[0][0]

answer = sol(N-1,M-1)

print(answer)