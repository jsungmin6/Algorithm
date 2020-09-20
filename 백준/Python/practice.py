#스타트 링크
#풀이계획
#BFS
#트리구조로 자식노드로 일정 수를 뺀수, 일정 수를 더한수가 있음
#BFS돌리기
###############################################################
from collections import deque
import sys
F, S, G, U, D = map(int,input().split())
need_visit=deque([S])
visit=[0]*1000001
while need_visit:
    node=need_visit.popleft()
    if node==G:
        print(visit[0:101])
        print(visit[node])
        sys.exit(0)
    #올라가려는 층 들른곳인지 체크, 전체층보단 적은지 체크
    if visit[node+U]==0 and (node+U)<=F:
        need_visit.append(node+U)
        visit[node+U]=visit[node]+1
    #내려가려는 층 들른곳인지 체크, 0층보단 큰지 체크
    if visit[node-D]==0 and (node-D)>0:
        need_visit.append(node-D)
        visit[node-D]=visit[node]+1
print('use the stairs')
