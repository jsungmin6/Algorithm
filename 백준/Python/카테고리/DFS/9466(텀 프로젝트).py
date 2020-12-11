'''
싸이클을 이루는 개수를 찾는 문제
visited 와 더불어 finished를 둬서 싸이클 여부를 확인한다.
'''
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(i):
    global cnt
    visited[i] = 1
    next_i = st[i]
    if visited[next_i]:
        if not finished[next_i]:
            cnt+=1
            temp = next_i
            while temp!=i:
                temp = st[temp]
                cnt+=1
    else:
        dfs(next_i)
    finished[i] = 1;

T = int(input())
for _ in range(T):
    n = int(input())
    st = [0]+list(map(int,input().split()))
    visited = [0]*(n+2)
    finished = [0]*(n+2)
    cnt=0
    for i in range(1,n+1):
        if not visited[i]:
            dfs(i)

    print(n-cnt)

    


