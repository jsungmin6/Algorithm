# 동전0

'''
Ai는 Ai-1의 배수 이기 때문에 그리디 알고리즘이 성립한다.
'''

import sys
input = sys.stdin.readline
N, K = map(int, input().split())
coins = [int(input()) for i in range(N)]

coins=coins[::-1]
count=0
for coin in coins:
    if K >= coin:
        coin_num = K//coin
        count+=coin_num
        K-=coin*coin_num
        if K == 0:
            break

print(count)