'''
풀이

연속하는 K 개의 신호등을 만들 수 있는 신호등의 수

arr[n] = 0~n까지 신호등 수를 기록하는 부분합 배열을 만든다.

k ~ n 까지 진행하면서 arr[n] - arr[n-k] 가 최소인 값을 찾는다.


'''

import sys
input = sys.stdin.readline
s
N,K,B = map(int,input().split())

arr = [0]*(N+1)

for i in range(B):
    arr[int(input())] = 1

s,e = 1,K
total = sum(arr[s:e+1])

answer = B
while True:
    if arr[s] == 1:
        total-=1
    e+=1
    s+=1

    if e == N+1:
        break

    total += arr[e]

    answer = min(total,answer)

print(answer)



import sys
input = sys.stdin.readline

N,K,B = map(int,input().split())

arr = [0]*(N+1)

for i in range(B):
    arr[int(input())] = 1

s=[]
cnt = 0
for i in range(N+1):
    cnt+=arr[i]
    s.append(cnt)

answer = B
for i in range(N+1-K):
    answer = min(answer,s[i+K] - s[i])

print(answer)