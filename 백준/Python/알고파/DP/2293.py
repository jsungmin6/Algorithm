#동전 1

#풀이 방법

'''
1,2,5 동전으로 10을 만드는 방법이라고 하면
10의 경우의 수 = (1,2를 이용해서 10을 만드는 방법 수) + (1,2,5를 이용해서 5를 만드는 방법) 이다.
(1,2를 이용해서 10을 만드는 방법 수) = (1을 이용해서 10을 만드는 방법 수) + (1,2를 이용해서 8을 만드는 방법 수 ) 이다.

'''

# # # # # # # # # # # # # # # # # # # # # 내 풀이
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
coins=[int(input()) for _ in range(n)]
dp=[0]*(k+1)

for coin in coins:
    for i in range(coin,k+1):
        if i == coin:
            dp[i]+=1 #처음엔 1을 더해주고 그 이후엔 이것을 이용해서 값을 추가해 줌.
        else:
            dp[i]=dp[i]+dp[i-coin]

print(dp[k])
