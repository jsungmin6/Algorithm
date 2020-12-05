'''
기준 박스 안에서 도토리가 몇개인지 체크하면서 범위를 좁혀나가는 이분탐색 문제이다.
cnt를 구할 때 range로 돌려서 구하면 시간초과가 남.
'''

import sys
input = sys.stdin.readline

N,K,D = map(int,input().split())
rules = []
lo=0
hi = N+1
for _ in range(K):
    rule= list(map(int,input().split()))
    rules.append(rule)


def solution(mid):
    cnt = 0
    for rule in rules:
        A,B,C = rule
        if A > mid:
            continue
        cnt += (min(B,mid) - A) // C + 1
    return cnt


while lo+1 < hi:
    mid=(lo+hi)//2
    c = solution(mid)
    # print('lo={}, hi={}, mid ={}, c={}'.format(lo,hi,mid,c))
    if c >= D:
        hi = mid
    else:
        lo = mid

print(hi)
