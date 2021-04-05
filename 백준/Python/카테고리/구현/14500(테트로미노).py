'''
모든 모양을 생각해서 시작점부터 끝점깢지 한바퀴씩 돌린다. 그리고 최댓값을 갱신한다.
도형모양 = 차지하는 공간[행,열],[...자신의 상대적 좌표들]
'''

a1 = [[1,4],[0,0],[0,1],[0,2],[0,3]]
a2 = [[4,1],[0,0],[1,0],[2,0],[3,0]]
b2 = [[2,2],[0,0],[1,0],[0,1],[1,1]]

c1 = [[3,2],[0,0],[1,0],[2,0],[2,1]] 
c2 = [[2,3],[1,0],[1,1],[1,2],[0,2]] 
c3 = [[3,2],[0,0],[0,1],[1,1],[2,1]] 
c4 = [[2,3],[0,0],[0,1],[0,2],[1,0]]

c5 = [[3,2],[2,0],[0,1],[1,1],[2,1]]
c6 = [[2,3],[0,0],[1,0],[1,1],[1,2]]
c7 = [[3,2],[0,0],[0,1],[1,0],[2,0]]
c8 = [[2,3],[0,0],[0,1],[0,2],[1,2]]

d1 = [[3,2],[0,0],[1,0],[1,1],[2,1]]
d2 = [[2,3],[1,0],[1,1],[0,1],[0,2]]
d3 = [[3,2],[0,1],[1,0],[1,1],[2,0]]
d4 = [[2,3],[0,0],[0,1],[1,1],[1,2]]
e1 = [[2,3],[0,0],[0,1],[0,2],[1,1]]
e2 = [[2,3],[0,1],[1,0],[1,1],[1,2]]
e3 = [[3,2],[0,1],[1,0],[1,1],[2,1]]
e4 = [[3,2],[0,0],[1,0],[2,0],[1,1]]

import sys
input =sys.stdin.readline

t_data = [a1,a2,b2,c1,c2,c3,c4,c5,c6,c7,c8,d1,d2,d3,d4,e1,e2,e3,e4]
N,M = map(int,input().split())
Map = [list(map(int,input().split())) for i in range(N)]
answer = 0

for t in t_data:
    t_r,t_c = t[0]
    t_li = t[1:]

    for i in range(M-t_c+1):
        for j in range(N-t_r+1):
            total = 0
            for l_r,l_c in t_li:
                total+=Map[j+l_r][i+l_c]
            answer = max(answer,total)

print(answer)


##dsf 백트래킹으로 구현한 코드

# dawitblog.tistory.com
from sys import stdin
input = stdin.readline

r,c = map(int,input().split())
mat = [list(map(int,input().split())) for _ in range(r)]

maxValue = max(max(mat))

visited = [[False]*c for _ in range(r)]
drc = [(1, 0), (0, -1), (-1, 0), (0, 1)]
# DFS
def dfs(k,s,tr,tc):
    global realMax

    # 나머지를 모두 최대값만 더했을때도 이미 저장된 값보다 작다면
    if s + maxValue*(3-k) <= realMax:
        return
    if k == 3:
        realMax = max(realMax,s)
        return

    for dr,dc in drc:
        newR = tr + dr
        newC = tc + dc

        if 0<=newR<r and 0<=newC<c and not visited[newR][newC]:
            if k == 1:
                visited[newR][newC] = True
                dfs(k+1,s+mat[newR][newC],tr,tc)
                visited[newR][newC] = False
            
            visited[newR][newC] = True
            dfs(k+1,s+mat[newR][newC],newR,newC)
            visited[newR][newC] = False

realMax = 0
for R in range(r):
    for C in range(c):
        visited[R][C] = True
        dfs(0,mat[R][C],R,C)
        visited[R][C] = False

print(realMax)