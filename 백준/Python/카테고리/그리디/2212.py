# 센서

'''
정렬한 후 거리가 제일 먼 곳부터 자른다.
'''

import sys
import heapq
input = sys.stdin.readline
N = int(input())
K = int(input())
sensors = sorted(list(set(list(map(int,input().split())))))

diffs=[]

if N==1:
    print(0)
    exit(0)

for i in range(len(sensors)-1):
    heapq.heappush(diffs,sensors[i]-sensors[i+1])

for _ in range(K-1):
    heapq.heappop(diffs)

print(-sum(diffs))


