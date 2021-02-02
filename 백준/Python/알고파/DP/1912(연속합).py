'''
dp[n] = max(dp[n-1]+arr[n],arr[n])
'''

n=int(input())
arr=list(map(int,input().split()))

dp=[-1000]*(n+3)
for i in range(1,len(arr)+1):
    dp[i+1] = max(dp[i]+arr[i-1],arr[i-1])

print(max(dp))