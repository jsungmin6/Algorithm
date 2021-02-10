'''
풀이
모두 서로를 왕래 가능, 절약할 수 있는 최대 액수 => 최소금액 구하라는 뜻
'''
import sys
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

while True:
    
    m,n = map(int,input().split())
    if m==0 and n==0:
        break
    road=[]
    total=0
    for _ in range(n):
        data = list(map(int,input().split()))
        road.append(data)
        total+=data[2]
    road.sort(key=lambda x:x[2])

    p=[-1]*(m+1)
    cost=0
    edge=0
    for i in road:
        if edge == m-1:
            break
        a,b,c = i
        if find(a) !=find(b):
            merge(a,b)
            cost+=c
            edge+=1

    print(total-cost)