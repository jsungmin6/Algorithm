N,M = map(int,input().split())
targets=list(map(int,input().split()))

from collections import deque

q=deque(i+1 for i in range(N))


def left():
    temp = q.popleft()
    q.append(temp)

def right():
    temp = q.pop()
    q.appendleft(temp)

cnt=0
for target in targets:
    idx = q.index(target)
    lc= idx
    rc= len(q)-lc
    if lc == 0:
        q.popleft()
    elif lc>rc:
        for _ in range(rc):
            right()
            cnt+=1
        q.popleft()
    else:
        for _ in range(lc):
            left()
            cnt+=1
        q.popleft()

print(cnt)
    
