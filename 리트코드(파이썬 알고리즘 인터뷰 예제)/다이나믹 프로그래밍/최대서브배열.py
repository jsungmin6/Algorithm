#최대서브배열

#풀이 방법

'''
다이나믹 프로그래밍
'''

# # # # # # # # # # # # # # # # # # # # #

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1] if nums[i-1] > 0 else 0
        return max(nusm)



# # # # # # # # # # # # # # # # # # # # # 카데인 알고리즘
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum=-sys.maxsize
        current_sum=0
        for num in nums:
            current_sum = max(num,current_sum+num)
            best_sum = (best_sum,current_sum)
        return best_sum
