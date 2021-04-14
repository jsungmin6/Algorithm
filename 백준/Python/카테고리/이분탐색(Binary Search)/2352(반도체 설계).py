'''
풀이
가장 긴 증가하는 수열 구하기
1.dp
2.이분탐색
'''
#dp
# n = int(input())
# arr = list(map(int,input().split()))
# dp = [1] * (n+1)

# for i in range(n):
#     for j in range(i):
#         if arr[j] < arr[i]:
#             dp[i] = max(dp[i],dp[j]+1)

# print(max(dp))

#이분탐색
import bisect
n = int(input())
arr = list(map(int,input().split()))
dp = [arr[0]]

for i in range(n):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        idx = bisect.bisect_left(dp,arr[i])
        dp[idx] = arr[i]

print(len(dp))


