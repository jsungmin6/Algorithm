#네트워크 연결

#풀이 방법

'''
전형적인 MST 문제
가중치(c)로 먼저 오름차순 정렬하고
a와 b의 대가리가 다를경우 (=같은 덩어리가 아닐경우) merge 해줌
'''

# # # # # # # # # # # # # # # # # # # # # 내 풀이
import sys
input=sys.stdin.readline

#find함수
def find(i:int):
    if uf[i]<0:
        return i
    uf[i]=find(uf[i])
    return uf[i]

#union함수
def merge(a,b):
    a=find(a)
    b=find(b)
    if a==b:
        return
    uf[b]=a


N=int(input())
M=int(input())
networks=[]
for _ in range(M):
    networks.append(list(map(int,input().split())))

#정렬
networks=sorted(networks,key=lambda x:x[2])

#union-find 진행
uf=[-1]*(N+1)
cost=0
for network in networks:
    a=network[0]
    b=network[1]
    c=network[2]
    if find(a)!=find(b):
        merge(a,b)
        cost+=c
print(cost)





###############################################다른풀이
'''
정렬하지 않고 우선순위 큐 사용해서 시간최소화
merge 할 때 덩어리끼리 레벨을 나눠서 작은 레벨의 덩어리가 큰 레벨의 덩어리 아래로 들어가게 엮음
'''
import sys
input=sys.stdin.readline
import heapq as h
n=int(input())
m=int(input())
pq=[]
for _ in range(m):
  a,b,c=map(int,input().split())
  h.heappush(pq,(c,a,b))
root=[i for i in range(n+1)]
level=[0]*(n+1)
def find(a):
  if root[a]==a:
    return a
  root[a]=find(root[a])
  return root[a]
def union(a,b):
  a=find(a)
  b=find(b)
  if a==b:
    return
  if level[a]<level[b]:
    root[a]=b
  elif level[a]>level[b]:
    root[b]=a
  else:
    root[a]=b
    level[b]+=1
cnt=0
ans=0
while 1:
  c,a,b=h.heappop(pq)
  if find(a)==find(b):
    continue
  cnt+=1
  ans+=c
  union(a,b)
  if cnt==n-1:
    print(ans)
    break
