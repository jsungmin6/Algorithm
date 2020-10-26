# 주사위 네개

# 풀이 방법

'''
if 문으로 순서대로 처리
문제를 잘 읽고 정리해야 함.
'''
# # # # # # # # # # # # # # # # # # # # # 내 풀이
import sys
import collections
input = sys.stdin.readline
N = int(input())
max_money = -sys.maxsize

for _ in range(N):
    dices = list(map(int, input().split()))
    count = collections.Counter(dices)
    if len(count) == 1:
        money = count.most_common(1)[0][0] * 5000 + 50000
    elif len(count) == 2:
        if count.most_common(2)[0][1] == count.most_common(2)[1][1]:
            money = count.most_common(
                2)[0][0]*500 + count.most_common(2)[1][0]*500 + 2000
        else:
            money = count.most_common(1)[0][0] * 1000 + 10000
    elif len(count) == 3:
        money = count.most_common(1)[0][0] * 100 + 1000
    else:
        money = max(dices) * 100

    max_money = max(max_money, money)

print(max_money)
