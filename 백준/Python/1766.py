import heapq

n=6
m=3

array=[[] for i in range(n+1)]
indegree = [0]*(n+1)

heap=[]
result=[]

data=[(3,1),(4,2),(6,5)]
for x,y in data:
    array[x].append(y)
    indegree[y]+=1

for i in range(1,n+1):
    if indegree[i]==0:
        heapq.heappush(heap,i)

print(array)
print(indegree)
print(heap)

result=[]

while heap:
    data = heapq.heappop(heap)
    result.append(data)
    for y in array[data]:
        indegree[y] -=1
        if indegree[y] ==0:
            heapq.heappush(heap,y)

for i in result:
    print(i,end=' ')
