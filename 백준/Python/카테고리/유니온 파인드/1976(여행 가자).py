'''
아이디어
유니온 파인드

근거
도시들의 개수와 도시들 간의 연결 여부(find)

풀이과정
1.union-find를 사용하여 0일때 union 1일때 find를 실행한다.

시간복잡도
유니온 파인드의 시간복잡도는 O(Mlog*N)이다.
'''

import sys

def find(n):
    if p[n] == -1:
        return n;
    p[n] = find(p[n])
    return p[n]

def merge(a,b):
    a=find(a)
    b=find(b)
    if a==b: return;
    if level[a] < level[b]:
        p[a] = b;
    elif level[b] < level[a]:
        p[b] = a
    else:
        p[b] = a;
        level[a]+=1

input = sys.stdin.readline

N=int(input())
M=int(input())
p=[-1]*(N+1)
level = [0]*(N+1)

for i in range(0,N):
    data = list(map(int,input().split()))
    for j in range(len(data)):
        if data[j] == 1:
            merge(i+1,j+1)

route = list(map(int,input().split()))

s = find(route[0])

for i in route[1:]:
    if s != find(i):
        print('NO')
        break
else:
    print('YES')


