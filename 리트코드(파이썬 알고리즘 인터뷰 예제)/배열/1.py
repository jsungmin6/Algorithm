#두수의 합

'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 105
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
'''

#풀이 방법

'''
1.간단한 방법이지만 여러 풀이 방법이 있음
'''

# # # # # # # # # # # # # #


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]


# # # # # # # # # # # # # #


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        #키와 값을 바꿔서 딕셔너리로 저장
        for i,num in enumerate(nums):
            nums_map[num]= i;

        #타겟에서 첫 번째 수를 뺀 결과를 키로 조회
        for i,num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target-num]:
                return nums.index(num), nums_map

# # # # # # # # # # # # # #


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for i, num in enumerate(nums):
            if target-num in nums_map:
                return [nums_map[target-num],i]
            nums_map[num]=i
