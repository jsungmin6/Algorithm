'''
블루레이에는 총 N개의 레슨이 들어가는데, 블루레이를 녹화할 때, 레슨의 순서가 바뀌면 안 된다
M개의 블루레이, M개의 블루레이는 모두 같은 크기
가능한 블루레이의 크기 중 최소를 구하는 프로그램

풀이 법:
최대치를 제시했을 때 이것이 가능한지 판단 하는 법.
ex ) M=3 이고 답을 15을 제시
1부터 차례대로 더해나가다가 다음수를 더했을 때 15가 넘어가는 지점에서 중단
1 2 3 4 5/ 6 7 / 8 / 9 => 4개 나오므로 불가 => 최대치를 올림

ex ) M=3 이고 답을 20을 제시
1 2 3 4 5 / 6 7 / 8 9 => 3개 나오므로 가능 => 최대치를 내림.

혹시 count 가 많아 최대치를 내리려던 중 레슨 시간을 초과하는게 있다면 그 블루레이의 용량의 크기가 최소이다.
# '''

# N,M = map(int,input().split())
# les = list(map(int,input().split()))

# lo = 0
# hi = sum(les)

# while lo+1<hi:
#     mid = (lo+hi)//2
#     if max(les) > mid:
#         hi=max(les)
#         break
#     total=0
#     count=1
#     for i in range(len(les)-1):
#         total += les[i]
#         if total + les[i+1] > mid:
#             count+=1
#             total=0
#     # print('lo : {}, hi : {}, mid : {}, count = {}'.format(lo,hi,mid,count))
#     if count > M:
#         lo = mid
#     else:
#         hi = mid

# print(hi)

import sys
input = sys.stdin.readline

def record(mid):
    count = 1
    temp = 0
    for i in L:
        temp += i
        if temp > mid:
            temp = i
            count += 1
    return count


N, M = map(int, input().split())
L = list(map(int, input().split()))
ans = 0
lo = max(L)
hi = sum(L)
while lo <= hi:
    mid = (lo + hi) // 2
    if M >= record(mid):
        ans = mid
        hi = mid-1
    else:
        lo = mid+1
print(ans)