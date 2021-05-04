'''
풀이

뭐지
'''
import sys
input =sys.stdin.readline

N = int(input())
arr = [int(input()) for i in range(N)]
max_num = max(arr)
max_idx = arr.index(max_num)
target = max_num-1
cnt=0
for i in range(max_idx,-1,-1):
    if arr[i] == target:
        cnt+=1
        target-=1
print(N-1-cnt)

