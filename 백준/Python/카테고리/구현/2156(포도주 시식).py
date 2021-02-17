'''
풀이
dp[n] = n번째까지 포도주에서 가장 많이 먹은 양
dp[n] = max(dp[n-1],dp[n-2]+arr[n],dp[n-3]+arr[n-1]+arr[n])
'''
import sys
sys.setrecursionlimit(10001)
input =sys.stdin.readline

n=int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

if n < 3:
    print(sum(arr))
    exit()

dp=[-1]*(n+2)
def drink(n):
    #리턴조건
    if n < 0:
        return 0
    if n == 0:
        return arr[0]
    if n == 1:
        return arr[0]+arr[1]
    if dp[n] !=-1:
        return dp[n]
    dp[n] = max(drink(n-1),drink(n-2)+arr[n],drink(n-3)+arr[n-1]+arr[n])
    return dp[n]

answer = drink(n-1)
print(answer)
