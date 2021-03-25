'''
풀이
N이 50 이하이므로 O(N^2)으로 풀어도 될 것 같다.
'''

import sys
input =sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))

for i in range(N):
    cx = arr[i][0]
    cy = arr[i][1]
    answer = 0
    for j in range(N):
        if i==j:
            continue
        tx = arr[j][0]
        ty = arr[j][1]

        if cx<tx and cy<ty:
            answer+=1
    print(answer+1,end=' ')