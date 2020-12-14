'''
그래프를 만들고 사이클을 찾자
'''

import sys
input =sys.stdin.readline

N,M,P = map(int,input().split())
graph=[0 for i in range(M+1)]
for _ in range(N):
    a,b = map(int,input().split())
    if not graph[b]:
        graph[b] = a


visited=[False for i in range(M+1)]

cnt=0
visited[P] = True
while graph[P] :
    visited[P] = True
    cnt+=1
    P=graph[P]
    if visited[P]:
        print(-1)
        exit()

print(cnt)
    