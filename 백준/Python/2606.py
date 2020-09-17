from collections import deque

C=int(input())
N=int(input())

arr=[[] for i in range(C+1)]

for _ in range(N):
    A,B = map(int,input().split())
    arr[A].append(B)
    arr[B].append(A)

print(arr)

temp=[0]*(C+1)

print(temp)

def bfs():
    visited=list()
    q=deque([1])
    while q:
        node = q.popleft()
        temp[node]=1
        for i in arr[node]:
            if temp[i]==0:
                q.append(i)

bfs()
print(sum(temp)-1)
