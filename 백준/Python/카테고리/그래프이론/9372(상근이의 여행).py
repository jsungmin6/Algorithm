'''
풀이
노드의 수인가?
'''
import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    N,M = map(int,input().split())
    for i in range(M):
        input()
    print(N-1)