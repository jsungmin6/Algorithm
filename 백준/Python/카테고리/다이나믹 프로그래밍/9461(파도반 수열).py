'''
[풀이]
이런 수열 dp 문제는 피보나치 형식이 많다.
dp[n] = dp[n-2]+dp[n-3] 이다.
'''

T = int(input())
dp=[1,1,1]

for _ in range(100):
    dp.append(dp[-2]+dp[-3])

for _ in range(T):
    print(dp[int(input())-1])

    