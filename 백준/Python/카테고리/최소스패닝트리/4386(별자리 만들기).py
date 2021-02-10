'''
풀이
모든 별을 이어야한다, 최소 비용을 구하라
MST의 냄새가 난다.
'''

import sys
import math
input = sys.stdin.readline

def find(n):
    if p[n] < 0:
        return n;
    p[n] = find(p[n])
    return p[n]

def merge(a,b):
    a=find(a)
    b=find(b)
    if a==b:
        return
    p[a] +=p[b]
    p[b] = a

def dist(i,j):
    x1,y1=points[i]
    x2,y2=points[j]

    return math.sqrt((x2-x1)**2 + (y2-y1)**2)


n=int(input())
points=[]
for _ in range(n):
    points.append(list(map(float,input().split(' '))))

graph=[]
for i in range(n):
    for j in range(i+1,n):
        graph.append([i,j,dist(i,j)])

graph.sort(key=lambda x:x[2])

p=[-1]*(n+1)

cost,edge = 0,0
for i in graph:
    a,b,c = i
    if find(a) !=find(b):
        if edge == n-1:
            break
        merge(a,b)
        cost+=c
        edge+=1

print(cost)

# n,f = str(cost).split('.')
# if len(f) > 2:
#     f = f[:2]

# print("{0}.{1}".format(n,f))