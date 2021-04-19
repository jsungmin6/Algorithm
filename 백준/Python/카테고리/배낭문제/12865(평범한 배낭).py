'''
풀이
냅색 디피
dp[i] = max(dp[i],dp[i-w]+v)
'''

# #개수가 무한일 때
# import sys
# input = sys.stdin.readline
# N,K = map(int,input().split())
# dp = [0]*(K+1)
# for _ in range(N):
#     W,V = map(int,input().split())

#     for i in range(W,K+1):
#         dp[i] = max(dp[i],dp[i-W]+V)
#     print(dp)

#개수가 1개씩 일 때
import sys
input = sys.stdin.readline
N,K = map(int,input().split())
dp = [[0 for i in range(K+1)] for j in range(N+1)]
for i in range(1,N+1):
    W,V = map(int,input().split())

    for j in range(1,K+1):
        if j-W < 0:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-W]+V)
    
print(dp[N][K])