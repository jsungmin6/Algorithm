#배열의 K번째 큰 요소

#풀이 방법

'''
heapq 모듈 이용
heapify 이용
nlargest 이용
정렬 이용
'''

# # # # # # # # # # # # # # # # # # # # heapify 이용
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        for _ in range(len(nums)-k):
            heapq.heappop(nums)

        return heapq.heappop(nums)
# # # # # # # # # # # # # # # # # # # # #

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k,nums)[-1]
