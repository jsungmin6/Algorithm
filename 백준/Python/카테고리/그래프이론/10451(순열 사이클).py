'''
풀이
무조건 사이클을 1개는 이룸
자식을 따라가다가 방문했던 녀석을 만나면 그것은 사이클이 이루어진 것
사이클이 이뤄질 때마다 1씩 더한다.
'''

import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    #방문검사
    N = int(input())
    visited = [0] * ( N + 1)
    p = list(map(int,input().split()))
    cnt = 0
    for i in range(1,N+1):
        #방문한 곳이면 스킵
        if visited[i]: 
            continue
        
        #방문
        visited[i] = 1

        #연결된 노드
        con = p[i-1]
        while not visited[con]:
            visited[con] = 1
            con = p[con-1]
        cnt+=1
    print(cnt)

    