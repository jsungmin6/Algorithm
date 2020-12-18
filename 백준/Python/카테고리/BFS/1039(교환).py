'''
1회 기회가 주어졌을 때
만들수 있는 모든 수를 만듬.

다음 기회에
그걸로 만들있는 모든 수를 만듬.

만들었던건 visited 에넣고 bfs 돌리는 식으로 풀이
중복이어도 상관 없음

나는 메모리초과가 나왔지만 정답과 큰 차이는 없는것 같은데 참 이상하다.
'''
from collections import deque
N,K = map(int,input().split())

N_l=len(str(N))
def bfs(N,K):
    q = deque([N])
    count=0
    temp=set()
    while q:
        q_size = len(q)
        for _ in range(q_size):
            node = q.pop()

            if count == K:
                return max(temp)
            else:
                temp=set()
            
            #새로운 후보들 생성해 next_node 에 넣어줌
            node_list=list(str(node))
            for i in range(N_l):
                for j in range(i+1,N_l):
                    node_list[i],node_list[j] = node_list[j],node_list[i]
                    new = ''.join(node_list)
                    node_list[i],node_list[j] = node_list[j],node_list[i]
                    if new[0] == '0':
                        continue
                    new=int(new)
                    if new not in temp:
                        temp.add(new)
                        q.append(new)
        count+=1
    return -1

print(bfs(N,K))
        


            
#정답코드

num, k = input().split()
k = int(k)
N = len(num)
S = {num}
for _ in range(k):
    if len(S)==0:break;
    new = set()
    while S:
        nums = list(S.pop())
        for i in range(N-1):
            for j in range(i+1,N):
                n = nums[:]
                n[i],n[j] = n[j],n[i]
                if n[0]!='0': new.add(''.join(n))
    S = new
if len(S)==0:print(-1)
else: print(max(S))