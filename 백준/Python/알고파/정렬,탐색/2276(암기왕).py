'''
풀이
이런 탐색과 확인은 리스트보다 set이 빠르다고 알고있다.

시간복잡도
O(1)
'''
import sys
input = sys.stdin.readline

T=int(input())
for _ in range(T):
    N = int(input())
    memo = set(list(map(int,input().split())))
    M = int(input())
    memory = list(map(int,input().split()))

    for i in memory:
        if i in memo:
            print(1)
        else:
            print(0)