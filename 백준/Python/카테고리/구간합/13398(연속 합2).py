'''
풀이
'''

n = int(input())
arr = list(map(int,input().split()))

#dp는 누적 합
#dp[0][i] = 제거 안함
#dp[1][i] = 1개 제거 한 경우
dp = [[0]*(n+2) for i in range(2)]
dp[0][0] = arr[0]
answer = -99999999999
if n==1:
    print(dp[0][0])
else:
    for i in range(1,n):
        # 아무런 원소를 제거하지 않았을 때, (이전까지의 연속합 + i번쨰 원소) 와 (i번째 원소)를 비교하여 큰 경우를 대입
        dp[0][i] = max(dp[0][i-1] + arr[i],arr[i])
        # 특정 원소를 제거하는 경우
        # i번째 원소를 제거하는 경우 :  dp[0][i - 1]
        # i번째 이전에서 이미 특정 원소를 제거하여 i번째 원소를 선택하는 경우 :  dp[1][i-1] + arr[i]
        dp[1][i] = max(dp[0][i-1], dp[1][i-1] + arr[i])

        answer = max(answer,dp[0][i],dp[1][i])
    print(answer)
    