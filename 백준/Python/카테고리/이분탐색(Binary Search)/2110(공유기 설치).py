import sys
input = sys.stdin.readline

N, C = map(int, input().split())
homes = sorted([int(input()) for i in range(N)])

lo = 0
hi = max(homes) - min(homes)+1


def home(mid):
    s = homes[0]
    count = 1
    for i in homes:
        if i >= s+mid:
            s = i
            count += 1
    return count


while lo+1 < hi:
    mid = (lo+hi)//2
    h = home(mid)
    # print('lo : {}, hi : {}, mid : {}, count = {}'.format(lo, hi, mid, h))
    if C > h:
        hi = mid
    else:
        lo = mid

print(lo)
