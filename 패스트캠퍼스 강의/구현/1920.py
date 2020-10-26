#수 찾기

#풀이 방법

'''
이분 탐색
'''
# # # # # # # # # # # # # # # # # # # # # 내 풀이

import sys
input = sys.stdin.readline
N=int(input())
A=set(map(int,input().split()))
M=int(input())
num=list(map(int,input().split()))

for i in range(M):
    if num[i] not in A:
        print(0)
    else:
        print(1)
# # # # # # # # # # # # # # # # # # # # #이분탐색
