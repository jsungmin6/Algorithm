'''
풀이
복사, 붙여넣기, 삭제 3가지 행위를 할 수 있다. 
3가지 행위를 하면서 목적지까지 최소시간이 걸려야 하니 bfs로 푼다.
큐 내부에 정보 세 가지를 넣는다. [현재이모티콘 수, 복사된이모티콘 수, 현재시간]

큐에는 경우의 수 3가지를 넣는다.
- 붙여넣기한 경우
- 삭제를 한 경우
- 복사만 한 경우

dp 리스트를 만듭니다.
dp[i] = i개의 이모티콘이 오는데 걸리는 최소 시간 입니다.

큐에서 현재시간이 >= dp[i] 인경우는 제외한다. 


'''
from collections import deque

def bfs(n):
    INF =987654321
    dp = [INF]*(n+1)
    dp[1] = 0
    q = deque([[1,0,0]])
    while q:

        imoge, copy, time = q.popleft()

        dp[imoge] = min(dp[imoge],time)
        
        #복사를 한 경우
        if imoge != copy:
            q.append([imoge,imoge,time+1])

        #삭제를 한 경우
        if dp[imoge-1] > time + 1 and imoge > 0:
            q.append([imoge-1,copy,time+1])
            # dp[imoge-1] = time + 1

        #붙여넣기
        if imoge+copy < n+1 and dp[imoge+copy] > time + 1 and copy > 0 :
            q.append([imoge+copy,copy,time+1])
            # dp[imoge+copy] = time + 1
    
    return dp[n]
n = int(input())
print(bfs(n))
