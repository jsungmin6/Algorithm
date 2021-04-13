'''
풀이
그리디

시간복잡도
정렬에 의해 O(NlogN)
'''
import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for i in range(N)]
arr.sort()
answer = 0

for i in arr:
    answer = max(answer,i * N)
    N-=1
print(answer)

