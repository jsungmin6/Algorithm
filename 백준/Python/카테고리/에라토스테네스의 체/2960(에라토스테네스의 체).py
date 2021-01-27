'''
풀이
에라토스테네스의 체

시간복잡도
nlogn
'''

N,K=map(int,input().split())
isPrime=[1 for i in range(N+1)]

cnt=0
for i in range(2,N+1):
    if isPrime[i]:
        for j in range(i,N+1,i):
            if isPrime[j]:
                isPrime[j] = 0
                cnt+=1
                if cnt==K:
                    print(j)
                    exit(0)