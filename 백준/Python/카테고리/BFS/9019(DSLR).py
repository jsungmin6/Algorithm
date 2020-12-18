'''
bfs 를 통해 접근
그런데 최소수를 구하는게 아니라 거기까지 도달하는데 있어서 방법들을 알아야 하니 배열을 만든후 거기에 방법을 저장해야 할 듯 하다.

L과 R에서 str로 변환하면 시간초과 발생하고
next_node= [] 를 만들어서 append 하고 for문돌려주는것도 시간초과 발생했다.
이렇게 해서 pypy로 간신히 통과
'''
from collections import deque

import sys
input = sys.stdin.readline

def bfs(A,B):
    v=[0]*10001
    v[A] = ''
    q=deque([[A,'']])

    while q:
        node,DSLR = q.popleft()

        # node가 B일 때 리턴
        if node == B:
            return DSLR

        # D
        result_D = (node*2)%10000
        if v[result_D] == 0 and 0<=result_D and result_D<10000:
            v[result_D] = v[node]+'D';
            q.append([result_D,v[result_D]])

        # S
        result_S = node-1
        if result_S == -1:
            result_S = 9999
        if v[result_S] == 0 and 0<=result_S and result_S<10000:
            v[result_S] = v[node]+'S';
            q.append([result_S,v[result_S]])

        # L
        result_L = (node % 1000) * 10 + node // 1000
        if v[result_L] == 0 and 0<=result_L and result_L<10000:
            v[result_L] = v[node]+'L';
            q.append([result_L,v[result_L]])

        # R
        result_R = (node % 10) * 1000 + node // 10
        if v[result_R] == 0 and 0<=result_R and result_R<10000:
            v[result_R] = v[node]+'R';
            q.append([result_R,v[result_R]])

T = int(input())
for _ in range(T):
    A,B= map(int,input().split())

    print(bfs(A,B))
