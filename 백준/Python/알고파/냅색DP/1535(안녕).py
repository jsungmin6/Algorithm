'''
풀이
냅색 풀이 도전
cache[i][j] = i번째 동전까지 고려했을 때 j원 만들 수 있는 경우의수
답 : cache[N][M]
cache[i][j] = cache[i-1][j] 경우의 수 일단 유지는 됨.
case1
i번째 동전만으로 채우는 경우
i가 10이면 10,20,30 의 경우는 경우의 수가 +1씩 추가
case2
i-1번째 동전까지 고려한 경우에 i번째 동전을 사용한 경우
cashe[i-1][j] 을 cashe[i][i의배수] 에 더해줘야함.

'''
import sys
input = sys.stdin.readline

N=int(input())
L=list(map(int,input().split()))
J=list(map(int,input().split()))
dp=[[0 for i in range(101)] for j in range(N+1)]
'''



for i in range(1,N+1):
    for j in range(1,101):
        if j-L[i-1] > 0:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-L[i-1]]+J[i-1])
        else:
            dp[i][j] = dp[i-1][j]
# print(dp)
print(dp[N][100])


# div = []
# for i in range(N):
#     div.append([J[i]//L[i],J[i]%L[i],L[i],i])
# div.sort(key=lambda x:(-x[0],-x[1],x[2]))

# h=100
# answer=0
# for data in div:
#     a,b,health,idx=data
#     temp = h - health
#     if temp <=0:
#         break
#     h = temp
#     answer+=J[idx]

# print(answer)
