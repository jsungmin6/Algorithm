'''
풀이
Map을 처음부터 끝까지 한번 순화한다.
각 좌표에서 bfs 를 실행해 max값을 갱신한다.
좌표를 포함한 4칸이 되는 모든 경우를 탐색한다.
dfs를 실행한 좌표는 제외하고 탐색한다.
각 탐색마다 visited를 만들고 백트래킹을 사용
=> 이 기법은 ㅏ ㅓ ㅜ ㅗ 이 모양을 만들 수 없다...
'''

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def check_in(x,y):
    if x<0 or y<0 or x==N or y==M:
        return False
    return True

def dfs(i,j,n,total):
    global maxnum
    visited[i][j] = True
    total += Map[i][j]
    if n==4:
        print("i,j,n,total : ",i,j,n,total)
        return total
    for k in range(4):
        new_i = i+dx[k]
        new_j = j+dy[k]

        if not check_in(new_i,new_j):
            continue
        if visited[new_i][new_j]:
            continue
        if dfs_check[new_i][new_j]:
            continue

        maxnum = max(maxnum,dfs(new_i,new_j,n+1,total))
        # total -= Map[new_i][new_j]
        visited[new_i][new_j] = False

    return maxnum

maxnum=0
N,M = map(int,input().split())
Map=[]
dfs_check=[[False for i in range(M)] for j in range(N)]
for _ in range(N):
    Map.append(list(map(int,input().split())))

answer = 0
for i in range(N):
    for j in range(M):
        visited=[[False for i in range(M)] for j in range(N)]
        answer = max(answer,dfs(i,j,1,0))
        print("answer:",answer)
        dfs_check[i][j] = True

print(answer)