'''
풀이
최대한 빨리 만나야하니 bfs를통해 최단경로를 구해준다.
'''
from collections import deque
A,B,N,M = map(int,input().split())

visited = [0]*100001
q = deque([N])
flag = False
while q:
    c = q.popleft()

    for i in [c+1,c-1,c+A,c+B,c-A,c-B,c*A,c*B]:
        if 0<= i <= 100000 and not visited[i]:
            visited[i] = visited[c] + 1

            if i == M:
                print(visited[i])
                flag = True
                break
            q.append(i)
    if flag:
        break

