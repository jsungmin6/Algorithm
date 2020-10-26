#복제 로봇

#풀이 방법

'''
1.나머지를 먼저 구하고 거기에 곱하기를 해줘도 됨.
'''

# # # # # # # # # # # # # # # # # # # # 내 풀이
import sys
input=sys.stdin.readline
A,B,C=map(int,input().split())

current = A%C
first = current
routine = [first]
routine_num=0
for i in range(B-1):
    next = (current*A)%C
    if next==first:
        routine_num=i+1
        break
    if next==0:
        print(0)
        exit(0)
    routine.append(next)
    current=next

if routine_num != 0:
    i=B%routine_num-1
    print(routine[i])
else:
    print(current)
