'''
풀이

소수찾기
'''

N=int(input())

prime = []
is_prime = [0]*(2000000)
is_prime[0]=1
is_prime[1]=1
for i in range(2,2000000):
    if is_prime[i]:
        continue
    else:
        for j in range(i*i,2000000,i):
            is_prime[j] = 1

def p(n):
    t = str(n)
    if t == t[::-1]:
        return True
    return False

for i in range(N,2000000):
    if is_prime[i] == 0 and p(i):
        print(i)
        break
        