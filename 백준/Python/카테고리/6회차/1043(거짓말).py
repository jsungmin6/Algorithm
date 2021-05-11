'''

'''
from collections import deque


N,M = map(int,input().split())

t = list(input().split())
true_man=deque([])
member = [[] for i in range(N+1)]
party = [[] for i in range(M+1)]
is_true = [0]*(N+1)
visited = [0]*(M)

if int(t[0]) > 0:
    for i in t[1:]:
        true_man.append(int(i))
        is_true[int(i)] = 1

# member : 어떤 사람이 어디 파티 참여했는지
# party : 어떤 파티에 누가 참여했는지

for i in range(M):
    partys = list(map(int,(input().split())))
    num = partys[0]
    members = partys[1:]
    party[i] = members
    for m in members:
        member[m].append(i)


while true_man:
    t = true_man.popleft()

    for p in member[t]:
        for m in party[p]:
            if is_true[m]:
                continue
            is_true[m] = 1
            true_man.append(m)
        visited[p] = 1

print(len(visited)-sum(visited))
            
