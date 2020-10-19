#군사 이동

#풀이 방법

'''
union find 에서 작은 값이 아니고 큰 값부터 넣어서 경로를 만들고
왕국과 왕국이 이어지면 종료. 이어진것은 find로 찾음
'''

# # # # # # # # # # # # # # # # # # # # # 내 풀이
import sys
input = sys.stdin.readline

def find(n):
    if uf[n] == n:
        return n;
    uf[n] = find(uf[n])
    return uf[n]

def union(a,b):
    a=find(a)
    b=find(b)
    if a==b :
        return
    uf[b]=a

p,w=map(int,input().split())
c,v=map(int,input().split())
graph=[]
uf=[i for i in range(p+1)]
for _ in range(w):
    start,end,width = map(int,input().split())
    graph.append([width,start,end])

#width 큰것부터 정렬
graph.sort(reverse=True)

#가장 작은 경로저장용 변수
width_min=sys.maxsize

#union find 진행
for way in graph:
    width,start,end = way[0],way[1],way[2]

    if find(start) != find(end):
        union(start,end)
        width_min=min(width_min,width)

    if find(c) == find(v):
        print(width_min)
        break
