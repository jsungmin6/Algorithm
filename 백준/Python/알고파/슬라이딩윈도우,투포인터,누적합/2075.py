#N번째 큰 수

#풀이 방법

'''
1.heap 자료구조에 넣음
heap 자료구조가 최댓값은 지원 안 하므로, 음수로 넣어주고 결과물에 다시 - 처리해줌. => 메모리초과

2.N개만큼 데이터를 받고 정렬 후 가장 작은 값보다 크면 데이터를 넣어줌
'''

# # # # # # # # # # # # # # # # # # # # # 내 풀이
import sys
import heapq

input=sys.stdin.readline
N=int(input())
heap=[]
heap_len=0
for _ in range(N):
    for num in list(map(int,input().split())):
        if len(heap)<N:
            heapq.heappush(heap,num)
        elif len(heap)==N and heap[0]<num:
            heapq.heappush(heap,num)
            heapq.heappop(heap)

print(heapq.heappop(heap))

# # # # # # # # # # # # # # # # # # # # # 다른 사람 풀이
'''
심플하게 sort로 계속 해줬어도 구할 수 있었음.
간단하게 생각해봐야 함.
'''
import sys
input = sys.stdin.readline

n = int(input())

q = list(map(int, input().split()))
for _ in range(n-1):
    q += list(map(int, input().split()))
    q = sorted(q, reverse=True)[:n]
print(q[n-1])
