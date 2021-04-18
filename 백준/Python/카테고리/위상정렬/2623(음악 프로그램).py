'''
위상정렬
'''
from collections import deque

N,M = map(int,input().split())
indegree = [0]*(N+1)
graph = [[] for i in range(N+1)]
for _  in range(M):
    temp = list(map(int,input().split()))
    K,arr = temp[0],temp[1:]
    for i in range(K-1):
        indegree[arr[i+1]]+=1
        graph[arr[i]].append(arr[i+1])

q = deque()
#위상 정렬 시작 : 큐에 indegree가 0인 정점을 다 넣음
for i in range(1,N+1):
    if not indegree[i]: q.append(i)

result =[]
#위상 정렬
# N번 시행해야 한다.
for i in range(0,N):
    print("i : ",i)
    print("result : ",result)
    # N번도 못 돌고 큐가 비면 사이클이 있어서 indegree가 0인게 없다는 뜻으로 위상정렬이 불가능 하다.
    if not q:
        print(0)
        exit()
    
    cur = q.popleft()
    result.append(cur)
    #인접한 정점을 순회하면서 indegree 1씩 감소. indegree가 0이 되면 큐에 넣음
    for n in graph[cur]:
        indegree[n] -= 1
        if indegree[n] == 0: q.append(n)

for i in result:
    print(i)
