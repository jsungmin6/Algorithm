'''
풀이
0,0 에서 N,M까지 경로의 수를 찾아주는 함수를 만든다.
'''
N,M,K = map(int,input().split())

dp = [[1 for i in range(16)] for j in range(16)]
for i in range(1,16):
    for j in range(1,16):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

if K == 0:
    print(dp[N-1][M-1])
else:
    r1 = K//M + 1
    c1 = K%M
    if c1 == 0:
        r1 -=1
        c1 = M
    print(dp[r1-1][c1-1] * dp[N-r1][M-c1])



