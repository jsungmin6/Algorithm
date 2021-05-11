from decimal import Decimal

# 입력.
N, K = map(int, input().split())
arr = list(map(int,input().split()))

# 파이썬은 느리므로 O(N2)으로 풀어야한다.
# (분산) = (제곱의 평균) – (평균) * (평균) 이라는 성질이 알려져 있습니다.
# 그러므로 누적 합 배열과 제곱의 누적 합 배열을 만들면, 쉽게 풀수있다.
sums = [0 for i in range(N+1)]
exps = [0 for i in range(N+1)]

# 누적 합, 제곱의 누적 합 설정.
for i in range(1, len(arr)+1):
    sums[i] = sums[i-1] + arr[i-1]
    exps[i] = exps[i-1] + arr[i-1] ** 2

# 결과값 설정.
re = Decimal('INF')
# K개 이상 수를 가지고 계산해야하기때문에 시작은 K개부터다.
# 누적 합의 배열 크기가 6
# (분산) = (제곱의 평균) – (평균) * (평균)
for i in range(K, N+1): # 즉 개수.
    # 개수 별로 계산한다.
    for j in range(N-i+1):
        mean = Decimal(sums[i+j] - sums[j]) / i
        var = Decimal(exps[i+j] - exps[j]) / i - mean * mean
        re = min(re, var)

print(re.sqrt())