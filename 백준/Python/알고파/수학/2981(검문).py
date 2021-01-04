'''
최대공약수의 약수들은 다 될것 왜냐면 나머지가 0으로 모두 같기 때문
그 후 최대공약수 ~ (두번째수-첫번째 수) 까지 숫자를 대입해보면서 나머지가 같은지 검사
=>실패

수학적인 풀이
A[N-1] - A[N] = M * (A[N-1] / M - A[N] / M )
A[1] - A[0] 에서 A[I] - A[i-1] 까지의 최대 공약수를 구하고 구해진 최대 공약수의 약수를 뽑아 내면 된다고 한다.
'''

from math import gcd
import sys
input = sys.stdin.readline
N=int(input())
num = []
for _ in range(N):
    num.append(int(input()))

num.sort()

diff=[]
for i in range(len(num)-1):
    diff.append(num[i+1]-num[i])

_gcd = diff[0]
for n in diff[1:]:
    _gcd = gcd(_gcd, n)

answer = set()
for i in range(2, int(_gcd**0.5)+1):
    if _gcd % i == 0:
        answer.add(i)
        answer.add(_gcd//i)
answer.add(_gcd)
answer = sorted(list(answer))
print(' '.join(map(str, answer)))

# from math import gcd
# import sys
# input = sys.stdin.readline
# N=int(input())
# num = []
# for _ in range(N):
#     num.append(int(input()))

# num.sort()
# _gcd = num[0]
# for n in num[1:]:
#     _gcd = gcd(_gcd, n)

# answer = [_gcd]

# for i in range(2,_gcd//2):
#     if _gcd//i == 0:
#         answer.append(i)

# for i in range(_gcd+1,num[1]-num[0]+1):
#     temp=[]
#     ch=True
#     for j in num:
#         if not temp:
#             temp.append(j%i)
#         else:
#             if j%i != temp[-1]:
#                 ch=False
#                 break
#     if ch:
#         answer.append(i)

# print(*answer)