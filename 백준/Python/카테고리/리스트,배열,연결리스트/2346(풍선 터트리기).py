'''
q문제
'''
import sys
from collections import deque
input = sys.stdin.readline


N= int(input())
data= list(map(int,input().split()))
answer=[]
balloons=deque()
for i,j in enumerate(data):
    balloons.append((j,i+1))

# print(balloons)

def left(q):
    temp = q.popleft()
    return q.append(temp)

def right(q):
    temp = q.pop()
    return q.appendleft(temp)


while balloons:
    n,i = balloons.popleft()
    answer.append(str(i))
    # print('balloons :',balloons)
    # print('answer :',answer)
    # print('n :',n)
    if len(balloons) == 0:
        break
    if n > 0:
        n=n-1
        n%=len(balloons)
        for _ in range(n):
            left(balloons)
    else:
        n=abs(n)
        n%=len(balloons)
        for _ in range(n):
            right(balloons)
print(' '.join(answer))

    


