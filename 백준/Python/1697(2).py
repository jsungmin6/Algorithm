N,K=int(input().split())

from collections import deque

def bfs(N,K):
    visited,need_visit=list(),list()
    mst=list()
    queue=deque()
    queue.append(N)
    while queue:
        node = queue.popleft()
        if node == K:
            return count
        else:
            queue.append(node-1)
            queue.append(node-1)
            queue.append(node-1)
