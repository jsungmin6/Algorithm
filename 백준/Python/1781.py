import heapq

N=int(input())
array=list()

for _ in range(N):
    array.append(list(map(int,input().split())))

array.sort()

answer=[]

for i in array:
    heapq.heappush(answer,i[1])
    if i[0]<len(answer):
        heapq.heappop(answer)

print(sum(answer))
