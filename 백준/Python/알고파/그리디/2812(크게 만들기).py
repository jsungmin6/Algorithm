# 증가한는 녀석이 있니? 체크
# 그러면 제일 뒷자리 제거

'''
stack 을 사용
S의 왼쪽부터 넣음
만약 stack의 top 보다 들어오려는게 크면 top을 제거하고 들어옴
만약 top 보다 작거나 같으면 들어옴
k가 남았으면 top부터 제거
'''

from collections import deque

N, K = map(int, input().split())
S = list(input())
stack = []

for i in S:
    if K==0:
        stack.append(i)
    else:
        while True:
            if not stack:
                stack.append(i)
                break
            if stack[-1] < i:
                stack.pop()
                K-=1
                if K==0:
                    stack.append(i)
                    break
            else:
                stack.append(i)
                break
    

while K != 0:
    K-=1
    stack.pop()

print(''.join(stack))
    
    
