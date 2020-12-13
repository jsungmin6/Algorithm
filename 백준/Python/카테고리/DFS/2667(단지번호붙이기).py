'''
dfs
'''
import heapq

N = int(input())
Map = [list(map(int,list(input()))) for i in range(N)]

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def dfs(r,c):
    Map[r][c] = 0
    cnt=1
    for i in range(4):
        new_r = r+dx[i]
        new_c = c+dy[i]

        if not ch_in(new_r,new_c):
            continue
        if Map[new_r][new_c]==0:
            continue
        
        cnt += dfs(new_r,new_c)
        
    return cnt

def ch_in(r,c):
    if r==N or c==N or r<0 or c<0:
        return False
    return True

answer = []
for r in range(N):
    for c in range(N):
        if Map[r][c] == 1:
            cnt = dfs(r,c)
            heapq.heappush(answer,cnt)

print(len(answer))
while answer:
    print(heapq.heappop(answer))