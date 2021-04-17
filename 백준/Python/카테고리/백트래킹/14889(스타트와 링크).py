'''
풀이
모든 조합을 구한후 조합에 해당하는 합을 구한후 차이값의 최솟값을 갱신해나간다
'''

import sys
input = sys.stdin.readline

n = int(input())
mat = [list(map(int,input().split())) for i in range(n)]

visited = [0 for _ in range(n)]
ans = 987564321

def dfs(idx,cnt):
    global ans
    if cnt == n//2:
        start,link =0,0

        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start += mat[i][j]
                elif not visited[i] and not visited[j]:
                    link += mat[i][j]
        
        ans = min(ans,abs(start-link))
    
    for i in range(idx,n):
        if visited[i] : continue

        visited[i] = 1
        dfs(i+1,cnt+1)
        visited[i] = 0
    
dfs(0,0)
print(ans)