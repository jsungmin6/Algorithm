#배열 파티션

'''
Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].
'''

#풀이 방법

'''
1.큰수끼리 min 해야 그나마 큰 수 남을 듯
2.sort 해서 두개씩 짝지어서 min 연산하고 결과값 더하면 될 듯
'''

# 내 풀이 # # # # # # # # # # # # #

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        answer=0

        for i in range(0,len(nums)-1,2):
            answer+=min(nums[i],nums[i+1])

        return answer

# 파이썬 다운 방식# # # # # # # # # # # # #
# sort하면 짝수번째가 항상 작은 수가 온다. 그 배열을 다 더해줌.
# [::2] 로 짝수번째 수만 정렬할 수 있다.
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])
