'''
큐 구현
'''
from collections import deque
import sys
input = sys.stdin.readline
N=int(input())
q=deque()
for _ in range(N):
    cmd = list(input().rstrip().split(' '))
    if cmd[0] == "push":
        q.append(cmd[1])
    elif cmd[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    elif cmd[0] == "back":
        if q:
            print(q[-1])
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(q))
    elif cmd[0] == "empty": 
        if q:
            print(0)
        else:
            print(1)
    else:# cmd[0] == "pop":
        if q:
            print(q.popleft())
        else:
            print(-1)