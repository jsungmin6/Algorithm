'''
풀이
시뮬레이션
'''
import sys
from collections import deque
input = sys.stdin.readline
cycles = [input().rstrip() for i in range(4)]
print(cycles)

def change(target,di):
    cycle = cycles[target]
    if di == -1:
        cycles[target] = cycle[1:] + cycle[0]
    else:
        cycles[target] = cycle[-1] + cycle[:-1]

def action(target,di):
    visited=[]
    next_target=deque([[target,di]])
    while next_target:
        t,d = next_target.popleft()
        visited.append(t)
        # target 의 next target을 찾는다.
        for i in [t+1,t-1]:
            # 양옆이면서
            if 0 <= i and i <= 3 and not i in visited:
                # N과 S가 달랐을 경우 
                if t < i: # 다음 타겟이 오른쪽일경우
                    if cycles[t][2] != cycles[i][6]: #N과 S가 달랐을 때
                        next_target.append([i,d*(-1)])
                else: #왼쪽 일 경우
                    if cycles[t][6] != cycles[i][2]: #N과 S가 달랐을 때
                        next_target.append([i,d*(-1)])
        
        # target을 di의 방향으로 돌린다.
        change(t,d)


for i in range(int(input())):
    target, di = map(int,input().split())
    target-=1

    action(target,di)

    print("i :",i," cycles : ",cycles)

print("cycles : ",cycles)
answer = 0
if cycles[0][0] == '1':
    answer+=1
if cycles[1][0] == '1':
    answer+=2
if cycles[2][0] == '1':
    answer+=4
if cycles[3][0] == '1':
    answer+=8
print(answer)
