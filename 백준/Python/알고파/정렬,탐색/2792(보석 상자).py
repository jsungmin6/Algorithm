'''
이분 탐색
'''

import sys
input=sys.stdin.readline

N,M = map(int,input().split())
nums=[]
for _ in range(M):
    nums.append(int(input()))


lo=1
hi=max(nums)

def solution(mid):
    cnt = 0
    for i in nums:
        if i%mid ==0:
            cnt+=i//mid
        else:
            cnt+=(i//mid)+1
    return cnt

ans = 0
while lo <= hi:
    mid=(lo+hi)//2

    cnt = solution(mid)

    # print('lo={}, hi={}, mid ={}, cnt={}'.format(lo,hi,mid,cnt))

    if N >= cnt:
        ans = mid
        hi = mid-1
    else:
        lo = mid+1

print(ans)