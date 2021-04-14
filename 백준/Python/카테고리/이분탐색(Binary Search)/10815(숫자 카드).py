'''
풀이
1. 일단 set in 으로
'''

N = int(input())
cards = set(map(int,input().split()))
M = int(input())
targets = list(map(int,input().split()))
answer = []
for t in targets:
    if t in cards:
        answer.append(1)
    else:
        answer.append(0)

print(*answer)