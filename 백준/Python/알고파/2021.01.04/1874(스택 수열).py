
import sys
input = sys.stdin.readline

N=int(input())
stack = []
result=[]
for _ in range(N):
    result.append(int(input()))

cnt=0
answer=[]
for i in range(1,N+1):
    if result[cnt]!=i:
        stack.append(i)
        answer.append('+')
    else:
        cnt+=1
        answer.append('+')
        answer.append('-')
        if stack:
            while result[cnt] == stack[-1]:
                cnt+=1
                stack.pop()
                answer.append('-')
                if not stack:
                    break
                if cnt == N:
                    break
if stack:
    print('NO')
else:
    for i in answer:
        print(i)
    
    