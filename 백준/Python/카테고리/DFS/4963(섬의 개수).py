'''
풀이
분리되어있는 컴포넌트의 수를 세는 흔한 dfs 문제

시간복잡도
O(V+E)
'''
import sys
sys.setrecursionlimit(2500)
input = sys.stdin.readline


dx=[0,0,1,-1,1,1,-1,-1]
dy=[-1,1,0,0,1,-1,1,-1]

def check_in(x,y,w,h):
    if x < 0 or y < 0  or x == h or y == w:
        return False
    # print("check_in : ",x,y,w,h)
    return True


def dfs(i,j,Map,visited,w,h):
    visited[i][j] = True
    for k in range(8):
        new_x = i+dx[k]
        new_y = j+dy[k]

        if not check_in(new_x,new_y,w,h):
            continue
        if visited[new_x][new_y]:
            continue
        if Map[new_x][new_y] == 0:
            continue
        
        dfs(new_x,new_y,Map,visited,w,h)


while True:
    w,h = map(int,input().split())
    if w==0 and h ==0:
        break
    Map = []
    for _ in range(h):
        Map.append(list(map(int,input().split())))
    
    visited=[[False for i in range(w)] for j in range(h)]

    lands=0
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and Map[i][j] == 1:
                
                dfs(i,j,Map,visited,w,h)
                lands+=1
    
    print(lands)
    
