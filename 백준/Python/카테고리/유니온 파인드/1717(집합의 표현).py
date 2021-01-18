'''
아이디어
유니온 파인드

근거
같은 집합에 포함되어 있는지 확인(find)
집합을 합친다(union)

풀이과정
1.union-find를 사용하여 0일때 union 1일때 find를 실행한다.

시간복잡도
유니온 파인드의 시간복잡도는 O(Mlog*N)이다.
'''
import sys
input = sys.stdin.readline

def find(n):
    if p[n] == -1:
        return n;
    p[n] = find(p[n])
    return p[n]


def merge(a,b):
    a = find(a)
    b = find(b)
    if a == b:
        return;
    p[b] = a

n,m = map(int,input().split())
p=[-1]*(n+1)

for _ in range(m):
    ch,a,b = map(int,input().split())
    if ch == 0:
        merge(a,b)
    if ch == 1:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')


