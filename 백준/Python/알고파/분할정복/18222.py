#투에-모스 문자열

#풀이 방법

'''
분할 정복, 점화식
2^(N)<x<=2^(N+1) 일 때,
F(x) = 1-F(x-N) 임을 보임을 몇개 적다 보면 알 수 있다.
ex)
F(5)=F(1) 의 반대 => F(5) = 1-F(1)
F(6)=F(2) 의 반대 => F(6) = 1-F(2)
F(8)=F(4) 의 반대 => F(8) = 1-F(4)
규칙을 보면 4씩 차이 난다. 이 4는 x가 4와 8사이에 있는 수라서 나온 규칙이다.
F(15)=1-F(7) 이다.
즉 2^(N)<x<=2^(N+1) 일 때, F(x) = 1-F(x-N) 이다.
'''
# # # # # # # # # # # # # # # # # # # # #

import sys
input = sys.stdin.readline
sys.setrecursionlimit(2000)
N=int(input())
limit=1000000000000000000

i=0
e=[]
while True:
    if 2**i < limit:
        e.append(2**i)
        i+=1
    else:
        e.append(2**i)
        break

def F(x):
    index=0
    if x==1:
        return 0
    if x==2:
        return 1
    for i in range(len(e)-1):
        if e[i]<x and x<=e[i+1]:
            index=i
            break
    return 1 - F(x-2**index)

print(F(N))
