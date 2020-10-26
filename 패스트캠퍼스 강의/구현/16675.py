# 두 개의 손

# 풀이 방법

'''
무조건 이기는 경우를 먼저 생각하고
나머지를 ? 로 처리
'''
# # # # # # # # # # # # # # # # # # # # # 내 풀이

# A가 이기면 true
import sys
import collections


def RSP(A, B):
    if A == 'S' and B == 'P' or A == 'P' and B == 'R' or A == 'R' and B == 'S':
        return True


input = sys.stdin.readline
ML, MR, TL, TR = input().split()

if RSP(ML, TL) and RSP(ML, TR) or RSP(MR, TL) and RSP(MR, TR):
    print('MS')
elif RSP(TL, ML) and RSP(TL, MR) or RSP(TR, ML) and RSP(TR, MR):
    print('TK')
else:
    print('?')
