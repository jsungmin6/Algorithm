#그냥 완전탐색 index범위만 유의

import sys
input = sys.stdin.readline

N,M = map(int,input().split())
Map=[]
for i in range(N):
    Map.append(list(input()))

max_l = min(N,M)
for n in range(max_l-1,-1,-1):
    # print('n:',n)
    for i in range(N-n):
        # print('i:',i)
        for j in range(M-n):
            # print('j:',j)
            if Map[i][j] == Map[i+n][j] == Map[i][j+n] == Map[i+n][j+n]:
                print((n+1)**2)
                exit()

