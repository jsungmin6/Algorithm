'''
등차수열 공식 이용한 이분탐색으로 인덱스 탐색
'''

import sys
input = sys.stdin.readline

def solve(n):
    return (n*(n+1))//2

T = int(input())
for _ in range(T):
    N = int(input())
    lo = 1
    hi = 10**16
    while lo+1 < hi:
        mid = (lo+hi)//2
        result = solve(mid)
        if result > N:
            hi = mid
        else:
            lo = mid
    print(lo)
    
