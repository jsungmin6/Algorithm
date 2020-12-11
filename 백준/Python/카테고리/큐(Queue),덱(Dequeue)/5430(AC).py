'''
덱을 만들어 그냥 구현 하면 될 것 같다.
'''

from collections import deque
import sys
input = sys.stdin.readline
T=int(input())
for _ in range(T):
    p = input().rstrip()
    n = int(input())
    x = deque(input().rstrip().replace("[","").replace("]","").replace(","," ").split(" "))


    if n ==0:
        x = deque([])

    ch=True
    r_flag = True
    
    for i in p:
        # print("x:",x)
        if i == 'R':
            r_flag = not r_flag
        elif i == 'D':
            if not x:
                ch=False
                break
            
            if r_flag:
                x.popleft()
            else:
                x.pop()
            

    if not ch:
        print('error')
    else:
        if not r_flag:
            x.reverse()
        temp = ','.join(x)
        print('['+temp+']')


