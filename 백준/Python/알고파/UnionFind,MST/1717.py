#집합의 표현

#풀이 방법

'''
유니온파인드 find 와 merge 사용
'''

# # # # # # # # # # # # # # # # # # # # # 내 풀이

#타고타고 올라가다가 결국 -1 인 녀석의 인덱스를 리턴함 = -1의 root를 리턴
def find(n):
    if (p[n] < 0):
        return n;
    p[n] = find(p[n]);
    return p[n]

#b가 a의 자식으로 들어감.
def merge(a,b):
    a=find(a);
    b=find(b);
    if(a==b):
        return
    p[b]=a;


import sys
input = sys.stdin.readline
n,m = map(int,input().split())

p=[-1]*(n+1)

for _ in range(m):
    k,a,b = map(int,input().split())
    if k==0:
        merge(a,b)
    else:
        if find(a)==find(b):
            print('YES')
        else:
            print('NO')
