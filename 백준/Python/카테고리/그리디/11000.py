# 강의실 배정

'''
끝나는 시간이 다음 시작시간보다 크다면 강의실을 추가해야한다.
'''


import sys
import heapq
input = sys.stdin.readline
N = int(input())
times = [list(map(int,input().split())) for _ in range(N)]

times.sort(key=lambda x: (x[0],x[1]))

start,end,count = 0,0,1
ends=[0]
for time in times:
    s,e = time
    min_ends = ends[0]
    if s < min_ends:
        count+=1
    else:
        heapq.heappop(ends)
    heapq.heappush(ends,e)
        

print(count)