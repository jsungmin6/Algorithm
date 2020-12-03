import sys
input = sys.stdin.readline

N,M = map(int,input().split())

amt = [int(input()) for _ in range(N)]
ans=0
lo = max(amt)-1
hi = sum(amt)

def record(mid):
    count = 1
    temp = 0
    for i in amt:
        temp += i
        if temp > mid:
            temp = i
            count += 1
    return count

while lo+1< hi:
    mid = (lo + hi) // 2
    count= record(mid)
    print('lo : {}, hi : {}, mid : {}, count = {}, ans = {}'.format(lo,hi,mid,count,ans))
    if count > M:
        lo = mid
    else:
        hi = mid
print(hi)
    