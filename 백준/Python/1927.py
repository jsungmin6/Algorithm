import heapq

n=int(input())
heap=[]
for _ in range(n):
    data=int(input())
    if data==0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap,data)

    
