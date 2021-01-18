'''
아이디어
우선순위 큐

풀이과정
1.최대힙 만든 후 N만큼 빼줌 -> 메모리초과
2.메모리 초과를 해결하기 우해 배열에 넣는 수를 최소화 해야한다.
배열의 크기를 N으로 고정
최대힙이므로 힙의 초댓값보다 큰 수들만 넣기로 함. 넣으면 배열에서 하나를 뺌.

시간복잡도
NlogN
'''

import sys
import heapq
input = sys.stdin.readline
heap=[]
N=int(input())
for _ in range(N):
    for num in list(map(int,input().split())):
        if len(heap)<N:
            heapq.heappush(heap,num)
        elif len(heap)==N and heap[0]<num:
            heapq.heappush(heap,num)
            heapq.heappop(heap)

print(heap[0])
