'''
count활용
'''
from collections import Counter

N = int(input())
cards = list(map(int,input().split()))
M = int(input())
targets = list(map(int,input().split()))
count_cards = Counter(cards)
answer=[]
for i in targets:
    answer.append(count_cards[i])
print(*answer)