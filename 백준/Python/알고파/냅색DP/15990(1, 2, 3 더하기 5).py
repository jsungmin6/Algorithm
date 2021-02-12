'''
풀이
냅색dp
2차원 dp를 사용
dp[i][j] = i번 숫자를 만드는데 마지막 숫자가 j인 경우의 수
'''
import sys
input = sys.stdin.readline

T = int(input())
dp = [[0 for i in range(4)] for j in range(100001)]
mod = 1000000009

dp[1]=[0,1,0,0]
dp[2]=[0,0,1,0]
dp[3]=[0,1,1,1]

for i in range(4,100001):
    dp[i][1] = (dp[i-1][2] + dp[i-1][3]) % mod
    dp[i][2] = (dp[i-2][1] + dp[i-2][3]) % mod
    dp[i][3] = (dp[i-3][1] + dp[i-3][2]) % mod


for _ in range(T):
    print(sum(dp[int(input())]) % mod)