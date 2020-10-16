#도시분할 계획

#풀이 방법

'''
전형적인 MST 문제
가중치(c)로 먼저 오름차순 정렬하고
a와 b의 대가리가 다를경우 (=같은 덩어리가 아닐경우) merge 해줌
'''

# # # # # # # # # # # # # # # # # # # # 내 풀이
import sys
import heapq
input=sys.stdin.readline



#find함수
def find(i:int):
    if uf[i]<0:
        return i
    uf[i]=find(uf[i])
    return uf[i]

#union함수 (레벨 나눠서 시간최적화)
def merge(a,b):
    a=find(a)
    b=find(b)
    if a==b:
        return
    if level[a]<level[b]:
        uf[a]=b
    elif level[a] >level[a]:
        uf[b]=a;
    else:
        uf[b]=a
        level[a]+=1


N,M=map(int,input().split())
level=[0]*(N+1)
houses=[]

#heapq로 정렬 시간 최적화
for _ in range(M):
    a,b,c=map(int,input().split())
    heapq.heappush(houses,(c,a,b))


#union-find 진행
uf=[-1]*(N+1)
cost=0
max_c=-sys.maxsize
cnt=0
while True:
    c,a,b=heapq.heappop(houses)
    if find(a)==find(b):
        continue
    merge(a,b)
    max_c=max(max_c,c)
    cost+=c
    cnt+=1
    if cnt == N-1:
        break;
print(cost-max_c)


#########################################################다른풀이
'''
하나씩 merge를 하면서 원하는 갯수만큼 연결이 되었을  종료를 시킴
'''

import sys
input=sys.stdin.readline
n,m=map(int,input().split())
e=[tuple(map(int,input().split())) for _ in range(m)]
e.sort(key=lambda t: t[2])
root=[i for i in range(n+1)]
level=[0]*(n+1)
def find(x):
  if root[x]==x: return x
  root[x]=find(root[x])
  return root[x]
def union(x,y):
  x,y=find(x),find(y)
  if x==y: return
  if level[x]>level[y]:
    root[y]=x
    level[y]=0
  else:
    root[x]=y
    if level[x]==level[y]:
      level[y]+=1
    level[x]=0
c,s=0,0
for x,y,d in e:
  print([x,y,d])
  if find(x)!=find(y):
    print([x,y,d])
    union(x,y)
    s+=d
    c+=1
    if c==n-2: break
print(s)
