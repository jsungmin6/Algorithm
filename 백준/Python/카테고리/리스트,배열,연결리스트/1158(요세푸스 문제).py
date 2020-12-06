'''
q로 구현
'''
from collections import deque

N,K = map(int,input().split())

dq = deque(i+1 for i in range(N))

answer =[]

def next(dq):
    temp = dq.popleft()
    return dq.append(temp)

# K 만큼 회전 0 인덱스 제거
while len(dq) != 0:
    for _ in range(K-1):
        next(dq)
    answer.append(dq.popleft())

# 출력
print('<',end='')
for i in range(N):
    if i != N-1:
        print('{}, '.format(answer[i]),end='')
    else:
        print('{}'.format(answer[i]),end='')
print('>')


#모법단안
# n, m = map(int, input().split())
# l = list(range(1, n + 1))
# r = []
# index = 0

# while l:
#     index = (index + m - 1) % len(l)
#     r.append(str(l.pop(index)))

# print('<', ', '.join(r), '>', sep='')