'''
풀이
'''
import sys
input  =  sys.stdin.readline

N,M = map(int,input().split())
S = set()
answer = 0
for i in range(N):
    S.add(input().rstrip())

for i in range(M):
    temp = input().rstrip()
    if temp in S:
        answer+=1

print(answer)