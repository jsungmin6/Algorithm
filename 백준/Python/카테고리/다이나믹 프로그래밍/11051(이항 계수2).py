'''
nCk = n-1Ck-1 + n-1Ck
'''
import sys
sys.setrecursionlimit(2000)

n,k = map(int,input().split())

dp=[[0 for i in range(n+1)] for j in range(n+1)]

def solution(n,k):
    if n==k or k==0:
        return 1
    if dp[n][k] != 0:
        return dp[n][k]
    result = (solution(n-1,k-1)%10007+solution(n-1,k)%10007)%10007
    dp[n][k] = result

    return result

print(solution(n,k)%10007)