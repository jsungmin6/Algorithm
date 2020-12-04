
import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lines = [int(input()) for i in range(K)]

lo = 0
hi = max(lines)+1


def record(mid):
    count = 0
    for line in lines:
        count += line//mid
    return count


while lo+1 < hi:
    mid = (lo+hi)//2
    c = record(mid)
    # print('lo : {}, hi : {}, mid : {}, count = {}'.format(lo, hi, mid, c))
    if N > c:
        hi = mid
    else:
        lo = mid

print(lo)
