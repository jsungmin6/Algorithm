'''
풀이
최소스패닝 트리 구현
'''

import sys
input = sys.stdin.readline

#union find 함수 정의
def find(n):
    if p[n] < 0:
        return n
    p[n] = find(p[n])
    return p[n]

def merge(a,b):
    a = find(a)
    b = find(b)
    if a==b: return
    p[a] += p[b]
    p[b] = a

V,E = map(int,input().split())
graph = []
p = [-1]*(V+1)
for i in range(E):
    A,B,C = map(int,input().split())
    graph.append([C,A,B])

#가중치 최소부터 정렬
graph.sort()
edge = 0
dist = 0

for mst in graph:
    # 연결된 edge가 node-1이라면 다 연결된 것
    if edge == V-1:
        break
    w,a,b = mst
    # 부모가 다르다면 연결해준다.
    if find(a) != find(b):
        merge(a,b)
        dist+=w
        edge+1

print(dist)