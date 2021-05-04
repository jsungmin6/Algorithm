'''
풀이

gems에서 gem을 차례대로 for에 넣는다.

q에 모든 요소가 들어가기 전에는 q에 계속 gem을 넣어준다.

q에 요소가 들어갈 때 dict에 요소의 수를 기록한다.

q에 모든 요소가 들어갔다면
- 다음 gem부터 q에 추가할 때 추가적으로 q의 첫번째 단어의 요소의 수를 확인한다.
- q의 첫번째 단어의 수가 2 이상이라면 현재 큐의정보를 pq에 저장한다. pq = [q길이,q시작 인덱스]
- gem을 q에 추가하고, q를 pop를 해주고 해당 요소의 수를 -1해준다.
- q의 첫번째 단어의 count를 다시 확인하며 위 과정을 반복한다.
- 첫 번째 단어의 count가 다시 1이 되었다면 for문을 진행한다.

우선순위 큐에서 우선되는 단어는 q의 길이가 가장 작으면서 q시작 인덱스가 가장 작은게 뽑힌다.

'''
from collections import defaultdict,deque
import heapq

def solution(gems):
    gem_set,now_set = set(gems), set()
    gem_dict = defaultdict(int)
    pq = []
    q = deque([])
    for i,gem in enumerate(gems):
        now_set.add(gem)
        gem_dict[gem]+=1
        q.append((i+1,gem))

        if len(now_set) == len(gem_set): # q에 모든 요소가 있다
            idx = q[0][0]
            l = len(q)
            heapq.heappush(pq,[l,idx])

            while gem_dict.get(q[0][1]) >= 2: # q의 첫번째 요소가 q안에 2개 이상이라면 while 문 진행
                idx,g = q.popleft()
                l = len(q)
                heapq.heappush(pq,[l,idx+1])
                gem_dict[g] -= 1

    l,s = heapq.heappop(pq)

    return [s,s+l-1]

print(solution(gems))