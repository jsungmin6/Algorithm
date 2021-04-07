'''
풀이
bfs 통해 다음 후보 리스트 생성
visited를 통해 거르면서 set에 답을 담는다.
'''

import sys
from collections import deque
input = sys.stdin.readline

answer = set()
visited = []
def bfs(a,b,c):
    visited = []
    q = deque([[a,b,c]])
    visited.append([a,b,c])
    while q:
        # print("q :",q)
        aq,bq,cq = q.popleft()

        if aq == 0:
            answer.add(cq)
        
        new_list=[]
        #a가 b에 붓거나 c에 붓거나
        new_list.append([max(0,aq-(B-bq)),min(bq+aq,B),cq])
        new_list.append([max(0,aq-(C-cq)),bq,aq+cq])
        #b가 a에 붓거나 c에 붓거나
        new_list.append([min(aq+bq,A),max(0,bq-(A-aq)),cq])
        new_list.append([aq,max(0,bq-(C-cq)),bq+cq])
        #c가 a에 붓거나 b에 붓거나
        new_list.append([min(aq+cq,A),bq,max(0,cq-(A-aq))])
        new_list.append([aq,min(bq+cq,B),max(0,cq-(B-bq))])

        # print("new_list :",new_list)

        for nl in new_list:
            if nl in visited:
                continue
            q.append(nl)
            visited.append(nl)

A,B,C = map(int,input().split())

bfs(0,0,C)

array=[]
for i in answer:
    array.append(i)
array.sort()
print(*array)


    
    