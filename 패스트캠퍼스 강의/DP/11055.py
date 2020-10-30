# 가장 큰 증가 부분 수열

# 풀이 방법

'''
DP문제
일차원 배열로 해결
DP[i]는 i번째 인덱스까지의 가장 큰 증가 부분 수열의 합이다.
'''

from copy import deepcopy

N = int(input())
A = list(map(int,input().split()))

DP=deepcopy(A)

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            DP[i] = max(DP[i],DP[j]+A[i])

print(max(DP))

#추가 배열 리스트 뽑기

# from copy import deepcopy

# N = int(input())
# A = list(map(int, input().split()))

# DP = deepcopy(A)
# rev = [i for i in range(N)]

# for i in range(N):
#     for j in range(i):
#         if A[i] > A[j] and DP[i] < DP[j] + A[i]:
#             DP[i] = DP[j] + A[i]
#             rev[i] = j


# idx = DP.index(max(DP))

# while rev[idx] != idx:
#     print(A[idx])
#     idx = rev[idx]

# print(A[idx])
