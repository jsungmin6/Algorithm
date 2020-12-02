
N = int(input())
A = list(map(int,input().split()))

DP=[0]*(N+1)
DP[0] = A[0]

for i in range(N):
    result = A[i]
    for j in range(i):
        DP[i] = result
        if A[i] > A[j]:
            result = max(result,DP[j]+A[i])
            DP[i] = result

print(max(DP))

# from copy import deepcopy

# N = int(input())
# A = list(map(int,input().split()))

# DP=deepcopy(A)

# for i in range(N):
#     for j in range(i):
#         if A[i] > A[j]:
#             DP[i] = max(DP[i],DP[j]+A[i])

# print(DP)