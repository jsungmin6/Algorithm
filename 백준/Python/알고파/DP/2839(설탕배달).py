'''
dp[n] = min(dp[n-3]+1,dp[n-5]+1)
'''


N=int(input())
MAX=10000

dp=[MAX]*(5001)
dp[3]=1
dp[5]=1

for i in range(6,N+1):
    if dp[i-3] != 0:
        dp[i] = min(dp[i],dp[i-3]+1)
    if dp[i-5] != 0:
        dp[i] = min(dp[i],dp[i-5]+1)

if dp[N] == MAX:
    print(-1)
else:
    print(dp[N])
