from collections import deque

N,M = map(int,input().split())
nums = deque([i for i in range(1,N+1)])
finds = list(map(int,input().split()))

def left():
    nums.append(nums.popleft())

def right():
    nums.appendleft(nums.pop())

cnt=0
for i in finds:
    target = nums.index(i)
    if len(nums)-target > target:
        for _ in range(target):
            left()
            cnt+=1
        nums.popleft()
    else:
        for _ in range(len(nums)-target):
            right()
            cnt+=1
        nums.popleft()

print(cnt)

