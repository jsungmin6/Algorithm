#회전 초밥

#풀이방법
'''
슬라이딩 윈도우로 돌리면서 보너스 쿠폰이 윈도우 내에 있는지 계속 체크하고 없으면 +1 해주고 max값 찾음
'''

# # # # # # # # # # # # # # # # # # # # # # # # # # #
import sys
input = sys.stdin.readline

N,d,k,c=map(int,input().split())
dish_list=[]
for _ in range(N):
    dish_list.append(int(input()))

dish_list=dish_list+dish_list[:k]

left=0
right=k

max_answer=0
while left<N:
    window=set(dish_list[left:right])
    answer=len(set(window))

    if not c in window:
        answer+=1

    max_answer=max(answer,max_answer)

    left+=1
    right+=1

print(max_answer)

# # # # # # # # # # # # # # # # # # # # # # # # # # # 빠른방법
'''
슬라이딩 윈도우로 돌리면서 보너스 쿠폰이 윈도우 내에 있는지 계속 체크하고 없으면 +1 해주고 max값 찾음
deque 사용하고 window를 고정해둔 후 left를 빼고 right를 추가하는 식으로 구성해 시간을 조금 더 줄임.
'''
from collections import deque
import sys
input = sys.stdin.readline

N,d,k,c=map(int,input().split())
dish_list=[]
for _ in range(N):
    dish_list.append(int(input()))

#리스트가 회전을 해 다시돌아와서 필요한 수만큼 회전초밥 리스트 늘려줌.
dish_list=dish_list+dish_list[:k]

left=0
right=k

#window 만듬
window=deque()
for i in dish_list[0:right]:
    window.append(i)

answer=len(set(window))

max_answer=answer

#슬라이딩 윈도우 진행
while left<N:
    left_str=window.popleft()
    right_str=dish_list[right]

    if not left_str in window:
        answer-=1

    if not right_str in window:
        answer+=1

    window.append(right_str)

    if not c in window:
        max_answer=max(answer+1,max_answer)
    else:
        max_answer=max(answer,max_answer)

    left+=1
    right+=1

print(max_answer)
