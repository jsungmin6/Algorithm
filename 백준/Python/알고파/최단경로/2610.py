# 회의준비

# 풀이 과정
'''
1.먼저 union find를 이용해서 그룹을 나눈다.
2.플로이드 와샬을 통해 각 지점들의 최단거리를 구한다.
'''

def find(n):
    if uf[n] < 0:
        return n
    uf[n] = find(uf[n])
    return uf[n]

def merge(a,b):
    a=find(a)
    b=find(b)
    if a==b:
        return
    uf[b]=a
    

import sys
input = sys.stdin.readline
N=int(input())
M=int(input())

uf=[-1 for i in range(N+1)]

dist=[[0 if i==j else sys.maxsize for i in range(N+1)] for j in range(N+1)]

for _ in range(M):
    #유니온 파인드
    a,b = map(int,input().split())
    if find(a) != find(b):
        merge(a,b)

    #플로이드 와샬
    dist[a][b] = 1
    dist[b][a] = 1


#플로이드 와샬 알고리즘
for k in range(N+1):
    for i in range(N+1):
        for j in range(N+1):
            dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])

#sys.maxsize 0 으로 바꿔 줌.
for i in range(N+1):
    for j in range(N+1):
        if dist[i][j] == sys.maxsize:
            dist[i][j] = 0

#그룹 나누기 위해 union find로 인해 만들어진 부모노드만 모아둠.
root_i=[]

for i in range(1,N+1):
    if uf[i] == -1:
        root_i.append(i)

#그룹의 수 출력
print(len(root_i))

#부모노드를 가르키는 애들을 같은 group 이라고 생각. group에 인덱스들이 모이면 dist에서 최대값이 최소인 행을 찾음.
# print(uf)
# print(root_i)
answer=[]
for i in root_i:
    group=[]
    for j in range(1,N+1):
        if find(j) == i:
            group.append(j)
    # print(group)
    max_way=[]
    for k in group:
        max_way.append(max(dist[k]))
    # print(max_way)
    answer.append(group[max_way.index(min(max_way))])

answer.sort()

for i in answer:
    print(i)
    



