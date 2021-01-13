from collections import deque
import sys
input = sys.stdin.readline

N=int(input())
graph=[[] for i in range(N+1)]
answer = [0]*(N+1)
for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
q=deque([1])
while q:
    parent=q.popleft()

    for i in graph[parent]:
        if not answer[i]:
            answer[i]=parent
            q.append(i)


for i in range(2,N+1):
    print(answer[i])

###
import sys

input = sys.stdin.readline


def solve():
    N = int(input())
    graph = [[] for _ in range(N+1)]
    result = [0]*(N+1)
    visited = [0]*(N+1)

    for _ in range(N-1):
        i, j = map(int, input().split())
        graph[i].append(j)
        graph[j].append(i)

    stack = [1]
    while stack:
        i = stack.pop()
        visited[i] = 1
        for j in graph[i]:
            if not visited[j]:
                result[j] = i
                stack.append(j)
    for i in range(2, N+1):
        print(result[i])


solve()