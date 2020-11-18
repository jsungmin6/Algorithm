# 곱셈

'''
만약 지수가 10 이면 5,5 이런식으로 분할 해서 각각의 나머지를 구한 후 합친 후 다시 나머지를 구하는 식으로 전체의 나머지를 구할 수 있다.
즉 분할정복으로 문제를 풀이할 수 있음.
'''


import sys
import heapq
input = sys.stdin.readline
sys.setrecursionlimit(2000)
A, B, C = map(int,input().split())

def solution(A,B,C):
    if B==1:
        return A%C

    temp = solution(A,B//2,C)%C

    if B%2==0:
        return (temp * temp)%C
    else:
        return (temp * temp*A%C)%C

print(solution(A,B,C))






