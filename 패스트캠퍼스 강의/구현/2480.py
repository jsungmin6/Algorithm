#주사위 세개

#풀이 방법

'''
if 문으로 순서대로 처리
'''
# # # # # # # # # # # # # # # # # # # # # 내 풀이
import sys
import collections
input = sys.stdin.readline
dices = list(map(int,input().split()))
count = collections.Counter(dices)

if len(count) == 1:
    print(count.most_common(1)[0][0] * 1000 + 10000)
elif len(count) == 2:
    print(count.most_common(1)[0][0] * 100 + 1000)
else:
    print(max(dices)* 100)
