'''
풀이
dp[i] = i번째 인덱스까지의 가장 큰 부분 배열 합
'''
import sys
input = sys.stdin.readline

def maximum_subarray(N:int,arr:list):
    dp = [0]*(N)
    dp[0] = arr[0]
    for i in range(1,N):
        dp[i] = max(dp[i-1]+arr[i],arr[i])
    print("dp :",dp)
    return max(dp)

T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
    
    print(maximum_subarray(N,arr))
