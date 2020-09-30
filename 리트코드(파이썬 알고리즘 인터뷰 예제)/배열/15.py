#세수의 합

'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
'''

#풀이 방법

'''
1.무식하게 풀기
2.안떠오름
'''

# # # # # # # # # # # # # #

from itertools import combinations

data=[-1,0,1,2,-1,-4]
answer=[]
for combination in combinations(data,3):
    combination=sorted(list(combination))
    if sum(combination) == 0 and combination not in answer:
        answer.append(list(combination))

print(answer)
