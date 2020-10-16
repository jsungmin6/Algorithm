#행성터널

#풀이 방법

'''
못 풀어서 블로그 참고
x,y,z축으로 각각을 정렬함
x축 인접 인덱스를 정점으로 하고 거리를 가중치로 둠. (y축, z축 반복)
이제 정점과 가중치 배열이 나왔으니 크루스칼 알골리즘 실행

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


N=int(input())
level=[0]*(N+1)
planet_points=[]
for _ in range(N):
    planet_points.append(list(map(int,input().split())))

#x,y,z축으로 정렬(사이값,인덱스)
line_x,line_y,line_z=[],[],[]
for i, planet_point in enumerate(planet_points,1):
    line_x.append([planet_point[0],i])
    line_y.append([planet_point[1],i])
    line_z.append([planet_point[2],i])

#정렬
line_x.sort()
line_y.sort()
line_z.sort()

#코스트와 정점으로 배열 변환
for i in range(len(line_x)-1):
    line_x[i] = [line_x[i+1][0]-line_x[i][0],line_x[i][1],line_x[i+1][1]]
    line_y[i] = [line_y[i+1][0]-line_y[i][0],line_y[i][1],line_y[i+1][1]]
    line_z[i] = [line_z[i+1][0]-line_z[i][0],line_z[i][1],line_z[i+1][1]]

#마지막 인덱스 제거(차이구하다 보면 1개가 남음 ex.5->4)
line_x.pop()
line_y.pop()
line_z.pop()

#각각 배열 합치고 정렬. 최종적으로 크루스칼 알고리즘 돌릴 리스트 만들어 줌.
mst_list=line_x+line_y+line_z
mst_list.sort()

#크루스칼 알고리즘 실행
uf=[-1]*(N+1)
cnt=0
cost=0
for planet in mst_list:
    c=planet[0]
    a=planet[1]
    b=planet[2]

    if find(a)!=find(b):
        merge(a,b)
        cost+=c
        cnt+=1

    if cnt==N-1:
        break;
print(cost)

##############################################################다른풀이 (시간단축)


import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
n=int(input())
root=[i for i in range(n+1)]
rank=[0 for _ in range(n+1)]
def find(a):
  if root[a]==a: return a
  root[a]=find(root[a])
  return root[a]
def union(a,b):
  a=find(a); b=find(b)
  if a==b: return
  if rank[a]<rank[b]:
    root[a]=b
  elif rank[a]>rank[b]:
    root[b]=a
  else:
    root[a]=b
    rank[b]+=1
pt=[(0,0,0)]+[tuple(map(int,input().split())) for _ in range(n)]
pts=list(enumerate(pt))[1:]
edge=[]
for i in range(3):
  pts.sort(key=lambda t: t[1][i])
  for j in range(n-1):
    edge.append((pts[j][0],pts[j+1][0],pts[j+1][1][i]-pts[j][1][i]))
edge.sort(key=lambda t: t[2])
mini=0
for u,v,w in edge:
  if find(u)!=find(v):
    union(u,v)
    mini+=w
print(mini)
