'''
풀이1 -> 실패

제일 긴 토막이 짧도록 만드려면
나무토막중 제일 긴 토막을 우선적으로 잘라야 한다.
자를때도 자를 수 있는 부위 중 최대한 중간에 있는 위치를 잘라야 한다.

우선순위 큐를 이용해 제일 긴 토막을 차례대로 뽑아낸다.
중간위치는 홀수일때 두 경우로 나뉜다. 하지만 문제 조건중 작은 것을 출력하라고 했으니 홀수일 경우 2로 나눴을때 몫에 해당하는 부분을 자른다.


풀이2

가장 긴 조각의 길이를 x라고 특정하자
긴 조각의 길이를 x로 만들기 위해 나무를 자른다.
- x를 고려해서 나무토막이 x보다 커지는 지점을 자른다. 
- 자르는 횟수가 c 이하라면 x를 키운다.
- 자르는 횟수가 c 보다 크다면 x를 줄인다.

뒤에서 부터 잘라서 처음 자르는 위치가 제일 작도록 한다.
만약 자르는 위치의 간격이 x보다 크다면 x가 최대길이인게 불가능하므로 종료처리한다.


'''

L,K,C = map(int,input().split())
cuts = [0,L] + list(map(int,input().split()))
cuts.sort()

def solution(x):
    cnt = 0
    cut_start = L
    prev=[]
    first = 0
    # x라는 길이를 넘으면 자른다.
    for i in range(len(cuts)-1,-1,-1):
        diff = cuts[i] - cuts[i-1]
        total = cut_start - cuts[i]
        if diff > x:
            return 10001,0
        elif total > x:
            cut_start = cuts[i+1]
            prev.append(cuts[i+1])
            cnt+=1
        else:
            continue
            
    if cnt < C:
        first = cuts[1]
    else:
        first = prev[-1]

    return cnt, first

lo = 0
hi = L
answer = 0
first_cut = 0
while lo <= hi:
    mid = (lo+hi)//2

    cnt,first = solution(mid)

    if C < cnt:
        lo = mid+1
    else:
        answer=mid
        first_cut = first
        hi = mid-1


print(answer,first_cut)



# import heapq
# import bisect
# L,K,C = map(int,input().split())
# cuts = list(map(int,input().split()))
# cuts.sort()

# pq = [] # 통나무 보관 [길이,시작인덱스,끝인덱스]
# heapq.heappush(pq,[L*(-1),0,L])

# def select_cut(s,e,arr):
#     mid = (s+e)//2

#     # print("mid : ",mid)

#     idx = bisect.bisect_left(arr,mid)

#     if idx == len(arr):
#         idx -=1

#     # print("idx : ",idx)

#     if idx > 0 and cuts[idx] - mid > mid - cuts[idx-1]:
#         idx -=1

#     return idx
    
# if K==1:
#     c = cuts[0]
#     l = max(L-c,c)
#     print(l,c)
#     exit()
    
# first_cut = L
# max_l = 0
# for i in range(C):
#     # 잘라야할 통나무 고르기
#     l,s,e = heapq.heappop(pq)
#     l = l*(-1)

#     if cuts[-1] <= s or cuts[0] >= e:
#         max_l = max(max_l,l)
#         continue

#     # 자를 위치 선정
#     idx = select_cut(s,e,cuts)
#     cut = cuts[idx]
#     # print("cut : " , cut)
#     # 첫 번쨰 자르는 위치 저장
#     first_cut = min(cut,first_cut)
#     #자른 통나무 양쪽 pq에 저장
#     heapq.heappush(pq,[(cut-s)*(-1),s,cut])
#     heapq.heappush(pq,[(e-cut)*(-1),cut,e])

# max_l = max(max_l,-pq[0][0])
# print(max_l,first_cut)
    



