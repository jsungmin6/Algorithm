N, M = map(int, input().split())

B = [i for i in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    B[a], B[b] = B[b], B[a]

for i in B[1:]:
    print(i, end=' ')
