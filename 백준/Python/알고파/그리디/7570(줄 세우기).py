'''
가장 긴 연속으로 증하가느 배열의 길이를 찾는다
1회 기회를 사용할 때마다 배열의 길이를 1씩 증가시켜야 한다.
즉 전체 어린의길이 - 연속으로 증가하는 배열의 길이가 답이다.
dp[n] = n 을 포함한 최장 수열 길이
'''
import sys
input = sys.stdin.readline

N = int(input())
childs = list(map(int,input().split()))
dp = [0]*(N+1)
answer = 0

for i in childs:
    dp[i] = dp[i-1]+1

print(dp)
print(N-max(dp))



# import sys
# input = sys.stdin.readline

# N = int(input())
# childs = list(map(int,input().split()))
# dp = [1]*(N+1)
# answer = 0

# for i in range(1,N):
#     # i-1의 인데스를 찾고 dp의 인덱스에 해당하는 값에 +1을 해준다. 만약 해당하는 인덱스가 없으면 1을 넣어줌
#     target = childs[i]-1
#     r = childs[:i]
#     if  target in r:
#         dp[i] = dp[r.index(target)]+1
#     else:
#         dp[i] = 1
#     answer = max(answer,dp[i])

# print(N-answer)








