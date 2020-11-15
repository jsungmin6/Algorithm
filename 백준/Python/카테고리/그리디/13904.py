# 과제 

'''
정렬한 후 들어올 때 겹치는 날짜가 들어오면 기존 배열에서 점수가 제일 작은놈을 바꾼다.
'''

import sys
import heapq
input = sys.stdin.readline
N = int(input())
sort_data =sorted([list(map(int,input().split())) for _ in range(N)], key=lambda x : x[0])

count=0

solve=[]
for d,w in sort_data:
    if d > count:
        heapq.heappush(solve,w)
        count+=1
    else:
        if w > solve[0]:
            heapq.heappop(solve)
            heapq.heappush(solve,w)

print(sum(solve))



