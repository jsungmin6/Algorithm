'''
풀이
피보나치 수열
'''
import sys
input = sys.stdin.readline

fibo = [(1,0),(0,1)]

for i in range(2,41):
    x1,y1 = fibo[i-2]
    x2,y2 = fibo[i-1]

    fibo.append((x1+x2,y1+y2))

T = int(input())
for _ in range(T):
    idx = int(input())
    print(*fibo[idx])

