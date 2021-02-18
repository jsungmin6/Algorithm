'''
풀이
스택

시간복잡도
O(N)
'''
import sys
input = sys.stdin.readline

stack=[]
for _ in range(int(input())):
    n = int(input())
    if not stack:
        stack.append(n)
    elif n==0:
        stack.pop()
    else:
        stack.append(n)
if stack:
    print(sum(stack))
else:
    print(0)