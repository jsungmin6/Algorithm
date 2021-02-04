'''
dp[n] = max(dp[n-1]+arr[n],arr[n])
'''

n=int(input())
arr=list(map(int,input().split()))

dp=[-1000]*(n+3)
for i in range(1,len(arr)+1):
    dp[i+1] = max(dp[i]+arr[i-1],arr[i-1])

print(max(dp))

##다른풀이
def find_max(arr, num):
    if num == 0:
        return 0
    tot = arr[0]
    max_tot = tot
    for i in range(1, num):
        if tot > 0 and tot + arr[i] >= 0:
            tot += arr[i]
        else:
            tot = arr[i]
        if max_tot < tot:
            max_tot = tot
    return max_tot

n = int(input())
a = list(map(int, input().split()))
print(find_max(a, n))

##다른풀이