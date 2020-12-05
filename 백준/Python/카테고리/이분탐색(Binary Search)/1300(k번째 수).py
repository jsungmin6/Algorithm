'''
n 이하의 숫자가 배열 안에 몇개 있는지 
'''

import sys
input = sys.stdin.readline

N=int(input())
k=int(input())

lo = 0
hi = N**2+1

def solution(mid):
    cnt = 0
    for i in range(1,N+1):
        temp = (mid-1)//i
        if temp > N:
            cnt+=N
        else:
            cnt+=temp
    return cnt

while lo+1 < hi:
    mid=(lo+hi)//2

    cnt = solution(mid)

    # print('lo={}, hi={}, mid ={}, cnt={}'.format(lo,hi,mid,cnt))

    if cnt >= k:
        hi = mid
    else:
        lo = mid

print(lo)
