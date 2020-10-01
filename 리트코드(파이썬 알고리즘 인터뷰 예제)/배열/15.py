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
3.투포인터
'''

# 브루트 포스 풀이# # # # # # # # # # # # #

from itertools import combinations

data=[-1,0,1,2,-1,-4]
answer=[]
for combination in combinations(data,3):
    combination=sorted(list(combination))
    if sum(combination) == 0 and combination not in answer:
        answer.append(list(combination))

print(answer)

##투 포인터 풀이 ###########################

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results=[]
        nums.sort()

        for i in range(len(nums)-2):
            #중복 값 건너뛰기
            if i> 0 and nums[i] == nums[i-1]:
                continue

            #간격을 좁혀가며 합 sum 계산
            left,right=i+1,len(nums)-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left+=1
                elif sum >0:
                    right-=1
                else:
                    results.append((nums[i],nums[left],nums[right]))

                    while left < right and nums[left] == nums[left+1]:
                        left +=1

                    while left < right and nums[right] == nums[right-1]:
                        right -=1

                    left +=1
                    right -=1
    return results
