'''
index를 계산해 커서위치를 특정해서 푸는 방법도 존재한지만 del과 insert 등에서 O(N)이 발생해 시간초과
stack 2개를 활용하면 pop와 append만으로 해결할 수 있으므로 매번 O(1)의시간이 든다.
'''

from collections import deque
import sys

from sys import stdin

stk1 = list(input())
stk2 = []
n = int(input())
for line in sys.stdin:
    if line[0] == 'L':
        if stk1: stk2.append(stk1.pop())
        else: continue
    elif line[0] == 'D':
        if stk2: stk1.append(stk2.pop())
        else: continue
    elif line[0] == 'B':
        if stk1: stk1.pop()
        else: continue
    elif line[0] == 'P':
        stk1.append(line[2])
print(''.join(stk1 + stk2[::-1]))