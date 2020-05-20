import heapq

n=int(input())
heap=[]
for _ in range(n):
    data=int(input())
    heapq.heappush(heap,data)

result=0

while len(heap)!=1:
    sum=heapq.heappop(heap)+heapq.heappop(heap)
    result+=sum
    heapq.heappush(heap,sum)

print(result)
