'''
풀이
bfs로 탐색
가장 먼 거리를 알아냄
가장 먼 거리인 헛간의 리스트를 알아 냄
'''
import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
graph = [[] for i in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def find_dist(start):
    visited = [0]*(n+1)
    visited[start] = 1
    q = deque([start])
    cnt = 0

    while q:
        q_size = len(q)
        cnt+=1
        for _ in range(q_size):
            node = q.popleft()
            
            for new_node in graph[node]:
                if visited[new_node]:
                    continue
                visited[new_node] = 1
                q.append(new_node)
    return cnt

def find_same_dist_list(dist):
    start = 1
    visited = [0]*(n+1)
    visited[start] = 1
    q = deque([start])
    cnt = 0
    same_dist_num = 0
    same_list = []


    while q:
        q_size = len(q)
        cnt+=1
        for _ in range(q_size):
            node = q.popleft()

            if cnt == dist:
                same_dist_num +=1
                same_list.append(node)
            
            for new_node in graph[node]:
                if visited[new_node]:
                    continue
                visited[new_node] = 1
                q.append(new_node)
    return same_list,same_dist_num

dist = find_dist(1)
same_list, same_dist_num = find_same_dist_list(dist)
print("same_list :",same_list)
print("same_dist_num :",same_dist_num)

print(min(same_list),dist-1,same_dist_num)
