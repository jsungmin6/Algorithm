#  1로 만들기

'''
다이나믹 프로그래밍
top down 방식은 메모리초과, 시간초과가 뜬다.
bottom up 방식으로 해결
'''
#bottom up
import sys
N = int(input())
dp =[sys.maxsize]*1000002
dp[1] = 0
for i in range(1,N+1):
    dp[i+1] = min(dp[i+1],dp[i]+1)
    if i*2< N+1:
        dp[i*2] = min(dp[i*2],dp[i]+1)
    if i*3< N+1:
        dp[i*3] = min(dp[i*3],dp[i]+1)

print(dp[N])

# #top down
# import sys
# sys.setrecursionlimit(100000)
# def dp(N):
#     if m[N]!=-1:
#         return m[N]
#     if N==1:
#         return 0

#     count = dp(N-1) + 1
#     if N%3 == 0:
#         count = min(count,dp(N//3) + 1)
#     if N%2 == 0:
#         count = min(count,dp(N//2) + 1)
#     m[N] = count
#     return count

# N = int(sys.stdin.readline())
# m =[-1]*1000001
# print(dp(N))
