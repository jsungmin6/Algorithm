'''
왼쪽 스택 같은 크기는 추가
오른쪽 스택 같은 크기는 넘어감
양쪽 더함
ok
'''
import sys
from collections import deque
input = sys.stdin.readline
N=int(input())
bar = [list(map(int,input().split())) for i in range(N)]
bar.sort(key=lambda x:x[0])

left=deque()
right=deque()
for i,size in bar:
    if not left:
        left.append([i,size])
    else:
        if left[-1][1] <= size:
            left.append([i,size])
        else:
            continue

for i,size in bar[::-1]:
    if not right:
        right.append([i,size])
    else:
        if right[-1][1] < size:
            right.append([i,size])
        else:
            continue

#계산
left_size=0
while left:
    i,size = left.popleft()
    if not left:
        left_size+=size
    else:
        left_size+=(left[0][0]-i)*size

right_size=0
while right:
    i,size = right.popleft()
    if not right:
        break
    right_size+=(i-right[0][0])*size

print(left_size+right_size)