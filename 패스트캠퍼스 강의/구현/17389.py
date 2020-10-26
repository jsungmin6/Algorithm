#보너스 문제

#풀이 방법

'''
그냥 구현
'''
# # # # # # # # # # # # # # # # # # # # #

import sys
input = sys.stdin.readline
N=int(input())
S=input()

bonus=0
answer=0
for i in range(len(S)-1):
    if 'X'==S[i]:
        bonus=0
    else:
        answer+=bonus
        answer+=i+1
        bonus+=1
print(answer)
