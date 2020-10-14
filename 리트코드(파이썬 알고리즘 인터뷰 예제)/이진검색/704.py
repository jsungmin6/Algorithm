#이진 검색

#풀이 방법

'''
이진검색 여러 방법으로 해보기
재귀풀이
반복풀이
라이브러리 사용
'''

# # # # # # # # # # # # # # # # # # # # # 재귀풀이
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if left <= right:
            mid = (left+right)//2

            if nums[mid] < target:
                return binary_search(mid+1,right)
            elif nums[mid] < target:
                return binary_search(left,mid-1)
            else:
                return mid
        else:
            return -1
    return binary_search(0,len(nums)-1)

# # # # # # # # # # # # # # # # # # # # # 반복풀이
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) //2

            if nums[mid] < target:
                left = mid +1
            elif nums[mid] > target:
                right = mid -1
            else:
                return mid
        return -1

# # # # # # # # # # # # # # # # # # # # # 이진검색모듈
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums,target)

        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1

# # # # # # # # # # # # # # # # # # # # # 이진검색 사용안하고 풀이
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            return -1
