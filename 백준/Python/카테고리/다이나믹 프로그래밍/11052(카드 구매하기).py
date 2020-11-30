'''
동전 문제랑 비슷하다.
dp[n] = 카드가 n개일 때의 최댓값
dp[1] = dp[0]+cards[0]
dp[2] = dp[1]+cards[0] or dp[0]+cards[1]
dp[3] = dp[2]+cards[0] or dp[1]+cards[1] or dp[0]+cards[2] 

'''
N = int(input())
cards = list(map(int,input().split()))
dp=[0]*(N+1)
for i in range(1,N+1):
    result = 0
    for j in range(1,i+1):
        k = dp[i-j]+cards[j-1]
        if k>result:
            result = k
    dp[i] = result

print(dp[N])