'''
버튼의 최소 횟수 -> bfs의 최단경로 구한는 방법과 같다
규칙을 잘 읽고 if문처리만 잘하면 될 듯
'''
from collections import deque



N,T,G = map(int,input().split())
visited = [0]*100001
visited[N] = 1
def bfs(N):
    q=deque([N])
    count = 0
    while q:
        q_size = len(q)



        for _ in range(q_size):
            now_node = q.popleft()

            if now_node == G:
                return count

            if now_node*2 > 99999:
                next_move = [now_node+1]
            else:
                m = list(str(now_node*2))
                m[0] = str(int(m[0])-1) if int(m[0])-1 > 0 else str(0)
                m = int("".join(m))
                next_move = [now_node+1, m]

            # if now_node == G:
            #     return count

            # if now_node*2 > 99999:
            #     next_node = -1 
            # elif now_node == 0:
            #     next_node = -1 
            # elif 0 < now_node*2 < 10 :
            #     next_node = now_node*2-1
            # else:
                # next_node = int(str(int(str(now_node*2)[0])-1)+str(now_node*2)[1:])
            # print("now_node",now_node)
            # print("next_node",next_node)

            for i in next_move:
                if 0<=i and i<=99999 and visited[i] == 0:
                    visited[i]=1
                    q.append(i)
            

        count+=1

        if count > T:
            break

    return "ANG"

print(bfs(N))