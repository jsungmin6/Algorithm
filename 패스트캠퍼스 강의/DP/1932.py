# 정수 삼각형 (S1)

# 풀이 방법

'''
DP문제
탐욕법 불가. 최댓값 찾아야 함.
반복문으로 해결
2차원 배열로 만듬
Dp[i][j] = max(Dp[i-1][j],Dp[i-1][j-1]) + A[i][j]
'''
# # # # # # # # # # # # # # # # # # # # # 내 풀이
# N = int(input())
# A = [[0 for i in range(N+1)] for _ in range(N+1)]
# # 제일 왼쪽 제일 위쪽에 0을 채워둔다. (점화식 적용 위함)
# DP = [[0 for i in range(N+1)] for _ in range(N+1)]

# for i in range(1, N+1):
#     temp = list(map(int, input().split()))
#     for j in range(1, len(temp)+1):
#         A[i][j] = temp[j-1]


# for i in range(1, N+1):
#     for j in range(1, N+1):
#         DP[i][j] = max(DP[i-1][j], DP[i-1][j-1]) + A[i][j]

# print(max(DP[N]))


##################################

def solution():
    import sys
    n = int(input())
    triangle = []
    for _ in range(n):
        triangle.append(list(map(int, sys.stdin.readline().rstrip().split())))
    accum = []
    for i in range(n):
        accum = [max(a+c, b+c) for a,b,c in zip([0]+accum, accum+[0], triangle[i])]
        print(accum)
    print(max(accum))


solution()
