'''
풀이
MST(최소스패닝 트리)
모두 연결, 최소 비용 계산
'''
import sys
input = sys.stdin.readline

N=int(input())
M=int(input())
network=[]
for _ in range(M):
    network.append(list(map(int,input().split())))

network.sort(key=lambda x:x[2])

def find(n):
    if p[n] < 0:
        return n
    p[n] = find(p[n])
    return p[n]

def merge(a,b):
    a=find(a)
    b=find(b)
    if a==b: return
    p[a] += p[b]
    p[b] = a

p=[-1]*(N+1)
cost=0
for n in network:
    a,b,c = n
    if find(a)!=find(b):
        merge(a,b)
        cost+=c
print(cost)
