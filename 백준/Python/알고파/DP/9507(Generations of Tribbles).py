'''
피보나치 수열 응용
'''
import sys
input = sys.stdin.readline


fibo = [-1]*70
fibo[0]=1
fibo[1]=1
fibo[2]=2
fibo[3]=4

def fi(N):
    if N < 2:
        return 1
    if N ==2:
        return 2
    if N ==3:
        return 4
    if fibo[N] != -1:
        return fibo[N]
    count = fi(N-1) +fi(N-2) + fi(N-3) + fi(N-4)
    fibo[N] = count

    return count

T = int(input())
for _ in range(T):
    t=int(input())
    if fibo[t] !=-1:
        print(fibo[t])
    else:
        fi(t)
        print(fibo[t])
