'''
dfs 탐색으로 몇개으 그래프가 있는지 탐색
for문으로 1번씩 방문하면 된다. 방문한곳은 넘어가기
'''
n=3
computers=[[1, 1, 0], [1, 1, 1], [0, 1, 1]]

def dfs(n,computers,visited):
    s=[n]
    while s:
        node = s.pop()
        
        for j in range(len(computers)):
            if computers[node][j] == 0:
                continue
            if visited[j]:
                continue
            visited[j] = 1
            s.append(j)



def solution(n, computers):
    visited=[0]*(n+1)
    answer=0
    for i in range(n):
        if not visited[i]:
            dfs(i,computers,visited)
            answer+=1
    return answer

print(solution(n, computers))