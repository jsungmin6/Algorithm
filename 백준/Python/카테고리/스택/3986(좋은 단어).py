'''
괄호랑 비스하다. 스택으로 풀이
'''
N=int(input())
cnt=0
for _ in range(N):
    S = list(input())
    stack=[]
    for i in S:
        if not stack:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
    if not stack:
        cnt+=1
print(cnt)
        

