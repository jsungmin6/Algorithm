from itertools import permutations
from itertools import product
N,K = map(int,input().split())
nums=list(input().split())
result =[]
for i in range(1,len(str(N))+1):
    per1 = product(nums, repeat=i)
    for j in per1:
        result.append(int(''.join(j)))

result.sort(reverse=True)

for i in result:
    if i <= N:
        print(i)
        break



##재귀
A = []
n, k = map(int,input().split())
elm = list(map(int,input().split()))

def dfs(x):
    if x > n: return
    A.append(x)
    for k in elm: dfs(10*x+k)

dfs(0)
print(max(A))


##
n,m=map(int,input().split())
a=[*map(int,input().split())]
def f(u):
    if u>n:return 0
    re=u
    for i in a:re=max(re,f(u*10+i))
    return re
print(f(0))