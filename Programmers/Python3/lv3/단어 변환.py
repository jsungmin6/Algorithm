'''
풀이
목적지까지의 최단거리이니 bfs로 진행한다.
bfs 로 해당하는 후보를 추가하면서 진행한다.
방문했던 후보는 기록한다.
만약 진행이 끝날때까지 target에 도달하지 못하면 0을 반환한다.
'''
from collections import deque
begin="hit"
target="cog"
words=["hio", "hoo", "coo", "cog"]

def bfs(begin, target, words):
    visited=[]
    cnt=0
    q=deque([begin])
    while q:
        #words 중 하나만 다르고 방문하지 않았던거를 q에 추가
        q_size=len(q)
        for _ in range(q_size):
            node = q.popleft()

            if node == target:
                return cnt

            for word in words:
                if word in visited:
                    continue
                ch=0
                temp = list(node)
                for i in word:
                    if i in temp:
                        temp.remove(i)
                    else:
                        ch+=1
                if ch != 1:
                    continue
                
                visited.append(word)
                q.append(word)
        cnt+=1
    return 0

def solution(begin, target, words):
    answer = bfs(begin, target, words)
    return answer

print(solution(begin, target, words))