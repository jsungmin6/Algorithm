'''
[풀이]
조건에 부합하는 조합을 구한다.
'''
from copy import deepcopy
import sys
input = sys.stdin.readline

N,P,E = map(int,input().split())

member = [0]*N
total = E

arr = [list(map(int,input().split())) for i in range(N)]
answer = []

def dfs(n,j,mn,mx,prev):
    global answer
    if answer:
        return 
    if n == P:
        if mn <=E and mx >= E:
            answer = deepcopy(prev)
            return
        else:
            return 
    
    for i in range(j+1,N):
        mn += arr[i][0]
        mx += arr[i][1]
        dfs(n+1,i,mn,mx,prev+[i])
        mn -= arr[i][0]
        mx -= arr[i][1]

dfs(0,-1,0,0,[])
if not answer:
    print(-1)
    exit()

for i in answer:
    member[i]+= arr[i][0]
    total-=arr[i][0]

for i in answer:
    diff = arr[i][1] - arr[i][0]
    if total >= diff:
        member[i] += diff
        total -= diff
    else:
        member[i] += total
        total = 0

print(*member)


