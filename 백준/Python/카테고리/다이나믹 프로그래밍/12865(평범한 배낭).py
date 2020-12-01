'''
array[i][j] 물먹을 i 개 받았고 최대무게가 j일때 가치의 최댓값
'''
import sys

N, K = map(int,sys.stdin.readline().split())
DP = {0:0} # 무게:가치
for _ in range(N):
    W, V = map(int,input().split())
    t = {}
    for w, v in DP.items():
        nw, nv = w + W, v + V
        if nw <= K and DP.get(nw,0) < nv:
            t[nw] = nv
    DP.update(t)
    print(DP)
print(max(DP.values()))



