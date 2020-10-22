#같은 수로 만들기

#풀이 방법

'''
분할 정복 문제이나 생각이 안난다.
오름차순과 내림차순 구간을 비교해서
계산이 필요할 때 처리하는 식으로 풀어보겠음.
'''
# # # # # # # # # # # # # # # # # # # # #

import sys
input = sys.stdin.readline
N=int(input())
stack=[]
up_index=[]
down_index=[]
stack.append(int(input()))
stack.append(int(input()))
down_index.append(-sys.maxsize)

answer=0
up_min=sys.maxsize
up_max=-sys.maxsize
for _ in range(N-1):
    number=int(input())
    stack_left_diff=stack[-2]-stack[-1]
    stack_right_diff=stack[-1]-number
    diff=stack_left_diff*stack_right_diff
    if diff<0:
        if stack[-1]<number:
            down_index.append(stack[-1])
    else:
        continue

    stack.append(int(input()))
