'''
[풀이]
i번째에 일을 선택해서 t[i] 번째 날까지 한 값 = max(i번째까지 한 최댓값 + p[i], 일 안하고 넘어간 경우 = dp[i+ t[i]])
'''

N = int(input())
dp=[0]*(N+1)
t,p = [],[]
for _ in range(N):
    ti,pi = map(int,input().split())
    t.append(ti)
    p.append(pi)

c_max = 0
for i in range(N):
    c_max = max(c_max,dp[i])
    if i+t[i] > N:
        continue
    dp[i+t[i]] = max(c_max + p[i],dp[i+t[i]])
print(max(dp))




