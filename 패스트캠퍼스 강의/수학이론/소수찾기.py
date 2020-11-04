def isPrime(N):
    for i in range(2,N):
        if N%2 == 0:
            return False
        if i*i > N:
            break
    return True
