# 부분수열의 합

'''
모든 조합 구해서 정답 나오는것 count
'''

import sys
import itertools

N, S = map(int, input().split())
nums = list(map(int, input().split()))
count=0
for i in range(1,len(nums)+1):
    for combination in itertools.combinations(nums,i):
        if sum(combination) == S:
            count+=1

print(count)