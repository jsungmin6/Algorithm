'''
lis 문제 푸는 방식
1.dp
2.이분탐색 사용

수가 충분히 작으니 dp로 품
'''

N=int(input())
arr=list(map(int,input().split()))

dp=[1]*(N+1)

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))