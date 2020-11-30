'''
동전 문제랑 비슷하다.
12 는 9+1+1+1 로 만들 수 있지만 4+4+4 가 더 최소다.
즉 모든 경우의 수를 생각해야 한다.
dp[n] = n일 때의 최소 경우의 수라고 하면
dp[1] = 1 => 1
dp[2] = 1+1 => 2
dp[3] = 1+1+1 => 3
dp[4] = 4 => 1
dp[5] = min(dp[4]+1,dp[1]+1)
dp[12] = min(dp[12-1]+1,dp[12-4]+1,dp[12-9]+1)
'''
import math

N = int(input())
nums = []
for i in range(1,int(math.sqrt(N))+1):
    if i**2 <= N:
        nums.append(i**2)

dp = [0]*(N+1)
dp[1] = 1

for i in range(2,N+1):
    result = 100000
    for num in nums:
        if i >= num:
            k=dp[i-num]+1
            if result > k:
                result = k
    dp[i] = result

print(dp[N])
