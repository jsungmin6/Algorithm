# 소수의 곱

# 풀이 방법

'''
2 3 5 7 이 있을 때 이것들을 소인수로 가지는 수들을 순서대로 구하는 방법은
2 3 5 7
2*2 2*3 2*5 2*7
3*2 3*3 3*5 3*7
5*2 5*3 5*5 5*7
7*2 7*3 7*5 7*7
2*2*2 2*3*3 2*5*5 2*7*7
...
이런식으로 후보의 가장 작은 수에 2, 3, 5, 7 을 곱해주는 순서를 만들면 된다.
heap을 사용한다.

set을 사용해서 일단 모든 값을 넣고 거르는 것은 시간초과가 발생한다.
그래서 값을 힙에 넣을 때부터 거르고 넣어야 한다.
\ 2 3 5 7 . . .
2 o x x x
3 o o x x
5 o o o x
7 o o o o
.
.
.
이런 구조라고 할때 모든 값을 구할 필요 없이 'o'표시 된곳만 구하면 될 것이다.
'''
# set 사용 -> 메모리 초과
# from copy import deepcopy
# import heapq

# K, N = map(int, input().split())
# p_lst = list(map(int, input().split()))
# ch = set()
# lst = deepcopy(p_lst)
# heapq.heapify(lst)

# T = 0
# while T < N:
#     mn = heapq.heappop(lst)
#     if mn in ch:
#         continue
#     ch.add(mn)
#     T += 1
#     for i in p_lst:
#         if mn*i < 2**32:
#             heapq.heappush(lst, mn*i)

# print(mn)

# set 사용 -> 메모리 초과
from copy import deepcopy
import heapq

K, N = map(int, input().split())
p_lst = list(map(int, input().split()))
lst = deepcopy(p_lst)
heapq.heapify(lst)

T = 0
while T < N:
    mn = heapq.heappop(lst)
    T += 1
    for i in p_lst:
        if mn*i < 2**32:
            heapq.heappush(lst, mn*i)
            if mn % i == 0:
                break
        else:
            break

print(mn)
