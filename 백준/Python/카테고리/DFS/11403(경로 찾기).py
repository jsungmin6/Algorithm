'''
dfs
'''
from collections import deque

N=int(input())
mat = [list(map(int,list(input().split()))) for i in range(N)]

def dfs(i):
    visit = mat[i]
    need_visit=deque()
    for v in range(N):
        if visit[v]==1:
            need_visit.append(v)
    while need_visit:
        # print("need_visit :",need_visit)
        node = need_visit.popleft()
        new_visit=mat[node]
        for j in range(N):
            if new_visit[j]==1:
                if not visit[j]:
                    need_visit.append(j)
                    visit[j] = 1
        
    return visit        

for i in range(N):
    for j in dfs(i):
        print(j, end =' ')
    print()