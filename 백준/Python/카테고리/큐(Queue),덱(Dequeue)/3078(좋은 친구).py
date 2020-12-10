'''
q를 2~20개 만들어 글자수에 맞춰 배열에 들어올 수 있도록 한다.
배열 안에는 녀석들의 인덱스만 들어있다.
들어올때 배열 top의 인덱스와 범위의 차가 K 이하이면 append, 이상이면 popleft() 로 가장 왼쪽을 제거하고 append 한다.
종료 후 남아있는 배열안 수의 총합을 체크
'''
from collections import deque
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
q_list = [deque() for i in range(21)]
cnt=0
for i in range(N):
    s = len(input())-1
    if not q_list[s]:
        q_list[s].append(i)
    else:
        while True:
            temp = q_list[s][0]
            if i - temp > M:
                q_list[s].popleft()
                if not q_list[s]:
                    break
            else:
                cnt+=len(q_list[s])
                break
        q_list[s].append(i)

print(cnt)

