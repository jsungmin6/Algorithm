#과반수 엘리먼트

#풀이 방법

'''
1.분할정복의 형태가 있다.
'''

# # # # # # # # # # # # # # # # # # # # 내 풀이
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]

        half = len(nums) //2
        a=self.majorityElement(nums[:half])
        b=self.majorityElement(nums[half:])

        return [b,a][nums.count(a) > half]


    # # # # # # # # # # # # # # # # # # # # 파이썬다운 방식
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]
