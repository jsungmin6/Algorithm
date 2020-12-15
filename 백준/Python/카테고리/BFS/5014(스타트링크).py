'''
'''

from collections import deque
F,S,G,U,D = map(int,input().split())

visited =[-1]*(F+1)

def bfs(i):
    visited[i] = 0
    count=0
    q=deque([i])
    while q:
        q_size = len(q)

        for c in range(q_size):
            node = q.popleft()

            if node == G:
                return count
            
            new_node = node+U
            if 0<new_node and new_node<F+1 and visited[new_node] ==-1:
                visited[new_node]=0
                q.append(new_node)

            new_node = node-D
            if 0<new_node and new_node<F+1 and visited[new_node] ==-1:
                visited[new_node]=0
                q.append(new_node)

        count+=1
    return 'use the stairs'

print(bfs(S))