'''
분류
그리디, 우선순위큐

근거
가장 작은 카드부터 더하는게 답이다.
sort로 정렬해 풀면 큐보다 시간이 더 걸린다. 왜냐하면 합친 결과를 다시 리스트에 넣어야 하기 때문.

풀이과정
우선순위 큐에 데이터를 넣고 두개씩 꺼낸후 결과를 다시 큐에 push한다. 마지막 남은게 정답

시간복잡도
O(NlogN)
'''
import sys
import heapq
input = sys.stdin.readline
N = int(input())
heap = []
for _ in range(N):
    heapq.heappush(heap,int(input()))

ans=0
while len(heap) != 1:
    print(heap)
    a=heapq.heappop(heap)
    b=heapq.heappop(heap)

    ans+=a+b

    heapq.heappush(heap,a+b)

print(ans)