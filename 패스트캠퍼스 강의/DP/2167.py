# 가장 큰 정사각형

# 풀이 방법
'''
점화식을 세우는게 관건.
이런 문제는 유형이라 많이 풀어보는 수 밖에 없다.
DP[i][j] 는 i,j 까지 만들 수 있는 가장 큰 정사각형의 한 변의 길이이다.
또한 i,j 지점이 정사각형이 되려면 [i-1,j][i,j-1][i-1,j-1] 이렇게 3개가 정사각형이어야 한다.
즉
DP[i][j] = min(DP[i-1][j],DP[i][j-1],DP[i-1][j-1]) + 1
'''

n, m = map(int, input().split())
A = [[0 for i in range(m+1)] for j in range(n+1)]
DP = [[0 for i in range(m+1)] for j in range(n+1)]

for i in range(n):
    for idx, j in enumerate(list(map(int, list(input())))):
        A[i+1][idx+1] = j

for i in range(n+1):
    for j in range(m+1):
        if A[i][j] != 0:
            DP[i][j] = min(DP[i-1][j], DP[i][j-1], DP[i-1][j-1]) + 1

print(max([max(i) for i in DP])**2)
