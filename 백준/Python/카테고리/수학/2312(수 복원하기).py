'''
N 이하의 소수리스트를 찾는다.
N을 큰 소수부터 안 나눠질 때까지 나눈다.

'''



T = int(input())
from collections import defaultdict
import sys
input = sys.stdin.readline

def prime(N):
    is_prime = [0]*(N+1)
    primes =[]
    for i in range(2,N+1):
        if is_prime[i]:
            continue
        else:
            for j in range(i*i,N+1,i):
                is_prime[j] = 1
    
    for i in range(2,N+1):
        if not is_prime[i]:
            primes.append(i)
    
    return primes

for _ in range(T):
    N = int(input())
    primes = prime(N)
    
    record = defaultdict(int)

    for p in primes:
        if N < p:
            break

        while N >= p:
            if N%p == 0:
                N//=p
                record[p]+=1
            else:
                break
    
    for k,v in record.items():
        print(k,v)