def era_prime(N):
    check, answer = [0 for i in range(N+1)], []
    for i in range(2, N+1):
        if check[i] == 0:
            answer.append(i)
        else:
            continue
        for j in range(i*i, N+1, i):
            check[j] = 1
    return answer


# 소인수의 개수 (1~N 까지의 소인수들의 개수를 보여줌)
def era_factor_count(N):
    A = [0 for i in range(N+1)]
    for i in range(1, N):
        for j in range(i, N, i):
            A[j] += 1
    return A

# 소읜수의 합


def era_factor_sum(N):
    A = [0 for i in range(N+1)]
    for i in range(2, N):
        for j in range(i, N, i):
            A[j] += i
    return A

# 소인수분해 하기
# 각 인덱스의 나눌 수 있는 가장 큰 소수가 옴.


def era_factorization(N):
    A = [0 for _ in range(N+1)]
    for i in range(2, N):
        if A[i]:
            continue
        for j in range(i, N, i):
            A[j] = i
    return A


# 소인수분해 활용.
print()
A = era_factorization(100)
N = 99
while A[N] != 0:
    print(A[N])
    N //= A[N]
