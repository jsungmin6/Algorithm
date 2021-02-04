'''
lis 문제 응용 배열을 출력하기
'''

N=int(input())
arr = list(map(int,input().split()))
dp=[1]*(N+1)

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i],dp[j]+1)

max_dp = max(dp)
print(max_dp)
max_idx = dp.index(max_dp)
answer=[]

while max_idx>=0:
    if dp[max_idx] == max_dp:
        answer.append(arr[max_idx])
        max_dp-=1
    max_idx-=1
answer.reverse()

print(*answer)
