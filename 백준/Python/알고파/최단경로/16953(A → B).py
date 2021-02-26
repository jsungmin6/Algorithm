'''
[풀이]
bfs로 풀면 된다 최솟값을 구하는 것이니 최소거리이다.
'''
from collections import deque

A,B = map(int,input().split())
visited=set()
q = deque([A])
cnt=0
while q:
    # print("q:",q)
    q_size = len(q)
    for _ in range(q_size):
        n = q.popleft()
        
        visited.add(n)

        if n == B:
            print(cnt+1)
            exit()

        for i in [n*2,n*10+1]:
            if i not in visited and i<=B:
                q.append(i)
    cnt+=1

print(-1)


