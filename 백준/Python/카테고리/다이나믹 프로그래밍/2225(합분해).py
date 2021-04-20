'''
풀이
K개를 더해서 N을 만든다.
dp[k][n] = k개를 이용해 n을 만드는 경우의 수
dp[k][n] = dp[k-1][0] + ...dp[k-1][n]
'''
N,K = map(int,input().split())
dp = [[1 for i in range(N+1)] for j in range(K+1)]

for i in range(2,K+1):
    for j in range(N+1):
        total = 0
        for k in dp[i-1][:j+1]:
            total += k%1000000000
        dp[i][j] = total%1000000000

print(dp[K][N])
    
