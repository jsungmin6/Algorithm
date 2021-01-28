'''
풀이
2^62 기에 배열을 만들고 시작하면 메모리 초과가 날 것 같다.
dict sort를 이용해본다.

'''

import sys
input = sys.stdin.readline

N=int(input())
cards = {}
for _ in range(N):
    num = int(input())
    if cards.get(num):
        cards[num]+=1
    else:
        cards[num]=1

cards_reverse = sorted(cards.items(),key=lambda item: (-item[1],item[0]))

print(cards_reverse[0][0])


'''
collections counter 이용
'''

# python3

import sys
from collections import Counter

num = int(sys.stdin.readline())
nlist = [int(x) for x in sys.stdin.read().split()]
ndict = Counter(nlist)
m = max(ndict.values())
for i in sorted(ndict.keys()):
	if ndict[i] == m:
		print(i)
		break