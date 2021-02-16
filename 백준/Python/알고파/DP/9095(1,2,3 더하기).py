'''
dp[n] = dp[n-1] + dp[n-2] + dp[n-3]
'''

T = int(input())
dp=[1,2,4]+[0]*11
# print(dp)


def solution(n):
    if dp[n] != 0:
        return dp[n]
    dp[n] = solution(n-1) + solution(n-2) + solution(n-3)
    return dp[n]

for _ in range(T):
    n = int(input())
    print(solution(n-1))
