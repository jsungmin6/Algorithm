import sys
input = sys.stdin.readline

N=int(input())
stack=[]
for _ in range(N):
    temp = input().rstrip().split(' ')
    if temp[0] == 'push':
        stack.append(temp[1])
    elif temp[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif temp[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif temp[0] == 'size':
        print(len(stack))
    else:#pop
        if stack:
            print(stack.pop())
        else:
            print(-1)




