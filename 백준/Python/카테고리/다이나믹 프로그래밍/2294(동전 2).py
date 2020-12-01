'''
d[n] = n일때 동전의 최소 개수 라고 하고 동전의 배열이 k 라고 한다면
d[n] = min(d[n-k[0]] ,d[n-k[1]]...) 이 아닐까 싶다.
'''

n,k = map(int,input().split())
coins= []
for _ in range(n):
    coins.append(int(input()))
dp = [0]*(k+1)

for i in range(1,k+1):
    result = 1000000
    for j in range(n):
        if i-coins[j] >= 0:
            result = min(result,dp[i-coins[j]]+1)
    dp[i] = result

if dp[k] != 1000000:
    print(dp[k])
else:
    print(-1)


        
    