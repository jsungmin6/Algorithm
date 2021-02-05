'''
풀이(블로그 참고)
pi를 math함수를 통해 구한다.
dp[i][j] = N 에서 i번빼고 pi를 j번 뺀 수
'''
# import math
# MOD=1000000000000000000

# N=int(input())

# pi=math.pi
# visited={}
# dp=[[0 for i in range(N+1)] for j in range(N+1)]
# def pibo(i,j):

#     p = N-1*i-pi*j

#     if p<=pi and 0<=pi:
#         return 1
#     elif p<0:
#         return 0
    
#     if dp[i][j]:
#         return dp[i][j]
    
#     dp[i][j] = (pibo(i+1,j) + pibo(i,j+1))%MOD

#     return dp[i][j] 

# print(pibo(0,0))

##내가 하려했던 풀이
import math

memo = {}

def fibo(x):
    if x in memo:
        return memo[x]
    if math.pi >= x >= 0:
        memo[x] = 1
    else:
        memo[x] = fibo(x-1) + fibo(x-math.pi)
    return memo[x]

n = int(input())
print(fibo(n)%1000000000000000000)