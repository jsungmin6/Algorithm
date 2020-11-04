def prime_factorization(N):
    i, answer = 2, []

    while i*i < N:
        if N % i == 0:
            answer.append(i)
            N //= i
        else:
            i += 1
    if N > 1:
        answer.append(N)
    return answer


print(prime_factorization(1234))
