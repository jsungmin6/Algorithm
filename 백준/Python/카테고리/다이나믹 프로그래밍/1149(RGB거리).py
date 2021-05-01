'''
풀이
dp[0] = R을 골랐을 때 지금까지의 최솟값
dp[1] = G을 골랐을 때 지금까지의 최솟값
dp[2] = B을 골랐을 때 지금까지의 최솟값
'''
import sys
input = sys.stdin.readline

N = int(input())
dp=[0,0,0]

for _ in range(N):
    r,g,b = map(int,input().split())
    dp[0],dp[1],dp[2] = min(dp[1],dp[2])+r,min(dp[0],dp[2])+g,min(dp[0],dp[1])+b

print(min(dp))