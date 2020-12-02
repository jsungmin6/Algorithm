'''
pypy로 실행
'''
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
trees = list(map(int,input().split()))

lo = 0
hi = max(trees)

while lo+1 < hi: #lo와 hi 사이에 한개는 있을 때 수행해야 함.
    mid = (lo+hi)//2
    sum = 0
    for i in trees:
        if i > mid:
            sum +=(i-mid)
    if M <= sum:
        lo = mid
    else:
        hi = mid
    
print(lo)