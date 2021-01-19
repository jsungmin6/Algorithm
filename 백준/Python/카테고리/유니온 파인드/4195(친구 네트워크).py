'''
아이디어
유니온 파인드

근거
친구 네트워크 연결

풀이과정
union 하면서 집합의 크기를 확인한다.

시간복잡도
유니온 파인드의 시간복잡도는 O(Mlog*N)이다.
'''
import sys
input = sys.stdin.readline

def find(n):
    if p[n] < 0: return n
    p[n] = find(p[n])
    return p[n]

def merge(a,b):
    a = find(a)
    b = find(b)
    if a == b: return
    p[a] += p[b]
    p[b] = a;

T = int(input())
for _ in range(T):
    name={}
    i=0
    F = int(input())
    friends=[]
    p=[-1]*(F*2+1)
    for __ in range(F):
        a,b = input().rstrip().split()
        friends.append([a,b])
        if not name.get(a):
            name[a] = i
            i+=1
        if not name.get(b):
            name[b] = i
            i+=1
    # print(name)
    for a,b in friends:
        # print(a,b)
        merge(name[a],name[b])
        # print('p :',p)
        print(-p[find(name[a])])


