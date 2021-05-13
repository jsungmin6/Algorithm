'''

풀이



'''

from collections import deque

N,K = map(int,input().split())
MAX = 100000+1

def bfs(N,K):
    visited = [0]*(MAX)
    visited[N] = 1
    time = 0
    min_time = MAX
    cnt= 0
    q = deque([[N,time]])
    while q:
            x,t = q.popleft()
            # print("x,t,cnt : ",x,t,cnt)

            visited[x] = 1

            if t > min_time:
                continue

            if x==K:
                if min_time == t:
                    cnt+=1
                elif min_time == MAX:
                    min_time = t
                    cnt+=1
            else:
                for nx in [x-1,x+1,2*x]:
                    if 0> nx or nx>=MAX:
                        continue
                    if visited[nx]:
                        continue
                    q.append([nx,t+1])

    return min_time,cnt

if N >= K:
    print(N-K)
    print(1)
else:
    min_time, ways =bfs(N,K)
    print(min_time)
    print(ways)


