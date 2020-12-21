def check(combStr):
    vowel = 0
    consonant = 0

    for char in combStr:
        if char in ['a', 'e', 'i', 'o', 'u']:
            vowel += 1
        else:
            consonant += 1

    if consonant >= 2 and vowel >= 1:
        return True
    else:
        return False


def solution(L, inputList, combStr, index):

    if len(combStr) is L:
        if check(combStr) is True:
            print(''.join(combStr))
        return

    if index >= len(inputList):
        return

    solution(L, inputList, combStr+list(inputList[index]), index + 1)
    solution(L, inputList, combStr, index + 1)


answer = 0
L, C = map(int, input().split())
inputList = list(map(str, input().split()))
inputList.sort()

combStr = []
index = 0

solution(L, inputList, combStr, index)


#부르트 포스
from itertools import combinations
l, c = map(int,input().split())
alpha = sorted(list(input().split()))

candidate = list(combinations(alpha,l))

for candi in candidate:
    num_v = 0
    num_c = 0
    for c in candi:
        if c in "aeiou":
            num_v +=1
        else:
            num_c +=1
    
    if num_v >=1 and num_c>=2:
        print(''.join(candi))