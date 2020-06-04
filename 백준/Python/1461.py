import heapq
N=7
M=2
array=[-37,2,-6,-39,-29,11,-28]

positive=[]
negative=[]

maxnum=max(max(array),-min(array))
#최대 값을 뽑아내야 함. positve에 마이너스를 붙여서 최솟값을 뽑아내면 그게 최댓값이다.

for i in array:
    if i>0:
        heapq.heappush(positive,-i)
    else:
        heapq.heappush(negative,i)


result=0

while positive:
    result-=heapq.heappop(positive)
    print(result)
    for _ in range(M-1):
        if positive:
            heapq.heappop(positive)

while negative:
    print(result)
    result-=heapq.heappop(negative)
    for _ in range(M-1):
        if negative:
            heapq.heappop(negative)


print(result*2-maxnum)
