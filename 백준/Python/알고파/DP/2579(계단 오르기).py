'''
풀이
dp[n] = n번째 계단에서 최댓값이라고 했을 때
dp 꼭대기 칸의 경우의 수는 2가지이다.
stair[n] + stair[n-1] + dp[n-3], stair[n] + dp[n-2]
둘 중에서 큰 것이 최댓값이다. 
'''
import sys
input = sys.stdin.readline

N= int(input())
stair = []
for _ in range(N):
    stair.append(int(input()))

dp=[0]*(N)
def st(n):
    if n == 0:
        return stair[0]
    if n == 1:
        return stair[0]+stair[1]
    if n < 0 :
        return 0
    if dp[n] != 0:
        return dp[n]
    dp[n] = max(stair[n] + stair[n-1] + st(n-3),stair[n] + st(n-2))
    return dp[n]

print(st(N-1))
