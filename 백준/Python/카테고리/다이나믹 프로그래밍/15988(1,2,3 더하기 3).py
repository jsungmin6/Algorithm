'''
풀이
1을 만드는 방법의 수 = 1
2를 만드는 방법의 수 = 2
3을 만드는 방법의 수 = 4
4를 만드는 방법의 수 = 1을 만드는 방법+ 3, 2를 만드는 방법+ 2, 3을 만드는 방법+1

dp[n] = dp[n-1] + dp[n-2] + dp[n-3]
'''

dp=[0,1,2,4]
for i in range(1000000):
    dp.append((dp[-3]+dp[-2]+dp[-1])%1000000009)
T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n])