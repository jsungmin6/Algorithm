'''
+1,-1,x2로 동시에 진행 bfs처럼 퍼져나감. 먼저 도착한곳이 최소경로이므로 bfs로 품
'''


from collections import deque

q = deque()

N,K = map(int,input().split())
visited=[0]*100001
count= 1
q.append(N)

def ch_in(node):
    if node <0 or node > 100000:
        return False
    return True 

if N==K:
    print(0)
    exit()

while q:
    q_size = len(q)
    for _ in range(q_size):
        node = q.popleft()

        if visited[node] == 1:
            continue

        visited[node] = 1

        if node-1 == K or node+1 ==K or node*2 ==K:
            print(count)
            exit()

        if ch_in(node-1) and visited[node-1] == 0: q.append(node-1)
        if ch_in(node+1) and visited[node+1] == 0: q.append(node+1)
        if ch_in(node*2) and visited[node*2] == 0: q.append(node*2)

    count+=1

print(count)

#더 깔끔한 푸리
from collections import deque

MAX=100001;
n, k = map(int, input().split())
array=[0]*MAX

def bfs(n):
    q=deque([n])
    while q:
        now_pos = q.popleft()
        if now_pos == k:
            return array[now_pos]
        for next_pos in (now_pos-1,now_pos+1,now_pos*2):
            if 0<=next_pos<MAX and not array[next_pos]:
                array[next_pos] = array[now_pos]+1
                q.append(next_pos)

print(bfs(n))
