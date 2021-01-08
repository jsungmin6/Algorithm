'''
답지 설명 한참 보고 이해함.
비트마스킹과 DP문제임
끝에 블록의 형태에 따라 그 전 블록을 경우의 수를 결정할 수 있다.
블록의 형태 위 중간 아래를 1 1 1 로 표시한다.
'''

N = int(input())

if N%2:
    print(0)
else:
    dp=[[0 for i in range(8)] for j in range(31)]
    dp[1][6] = 1
    dp[1][3] = 1
    dp[1][0] = 1
    for i in range(2,N+1):
        dp[i][0] = dp[i-1][7]
        dp[i][1] = dp[i-1][6]
        dp[i][3] = dp[i-1][4]+dp[i-1][7]
        dp[i][4] = dp[i-1][3]
        dp[i][6] = dp[i-1][1]+dp[i-1][7]
        dp[i][7] = dp[i-1][0]+dp[i-1][3]+dp[i-1][6]
    
    print(dp[N][7])
