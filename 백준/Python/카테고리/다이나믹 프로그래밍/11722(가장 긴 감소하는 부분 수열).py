'''
풀이
DP로 풀이
dp 배열에 가장 긴 감소한는 부분 수열의 수를 저장
'''

N= int(input())
arr = list(map(int,input().split()))
dp=[1]*(N+1)


for i in range(N):
    for j in range(i): # 타겟 idx의 전 idx들을 탐색
        if arr[i] < arr[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))

#### 2진탐색 활용

import bisect

x = int(input())
arr = list(map(int, input().split()))

dp = [arr[0]]

for i in range(x):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        idx = bisect.bisect_left(dp, arr[i])
        dp[idx] = arr[i]
    print("dp : ",dp)

print(len(dp))