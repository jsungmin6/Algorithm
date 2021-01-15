'''
Ai = A⌊i/P⌋ + A⌊i/Q⌋ (i ≥ 1)
점화식이 주어졌다.
DP문제이다.
dp[N] = dp[N//P] + dp[N//Q]
N이주어졌고 dp[0] = 1 이 주어졌으니 top down 방식으로 접근해야 할듯 하다(재귀)
'''
import sys
sys.setrecursionlimit(2000)
N,P,Q = map(int,input().split())
dp={}
dp[0] = 1
def topdown(n):
    if n == 0:
        return 1
    if dp.get(n):
        return dp[n]
    count = topdown(n//P) + topdown(n//Q)
    dp[n] = count

    return count

topdown(N)
print(dp[N])