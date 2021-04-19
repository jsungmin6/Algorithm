'''
풀이
dp[i] = i의 용량을 확보하기 위한 앱 비활성화의 최소의 비용
dp[i][j] = min(dp[i],dp[i])
'''
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
m = [0]+list(map(int,input().split()))
c = [0]+list(map(int,input().split()))
total = sum(c)
dp = [[0 for i in range(total+1)] for j in range(N+1)]
result = total
for i in range(1,N+1):
    for j in range(1,total+1):
        if j < c[i]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-c[i]] + m[i])
    
        if dp[i][j] >= M:
            result = min(result,j)

print(result)