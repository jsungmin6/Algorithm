'''
bfs를 통해 2단계 내에 있는 수를 출력
'''
import sys
from collections import deque

def bfs(s):
    v = [0] * (n+1)
    q = deque([s])
    cnt=0
    c = 0
    v[s] = 1
    while q:
        if c == 2:
            return cnt
        q_size = len(q)
        c+=1
        for _ in range(q_size):
            friend = q.popleft()
            for i in graph[friend]:
                if not v[i]:
                    cnt+=1
                    q.append(i)
                    v[i] = 1
    return cnt


input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for i in range(n+1)]
start = 1
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs(1))


