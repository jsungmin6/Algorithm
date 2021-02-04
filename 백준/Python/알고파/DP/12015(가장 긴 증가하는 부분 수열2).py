'''
lis 의 이분탐색 사용
'''

import bisect

N = int(input())
arr = list(map(int,input().split()))
dp=[arr[0]]

for i in arr:
    if i > dp[-1]:
        dp.append(i)
    else:
        idx = bisect.bisect_left(dp,i)
        dp[idx] = i

print(len(dp))