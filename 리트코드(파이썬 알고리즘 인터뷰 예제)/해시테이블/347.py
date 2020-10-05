#상위 K 빈도 요소

'''
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.
'''

#풀이 방법

'''
1.counter 사용
2.set과 count 사용
'''

# # # # # # # # # # # # # # # # # # # # # 내 풀이
import collections

nums=[1,1,1,2,2,3]
k=2
array=[]
freq=collections.Counter(nums)


# # # # # # # # # # # # # # # # # # # # # heap 활용. 최댓값이라서 -로 값 넣음.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        freqs_heap = []
        # 힙에 음수로 삽입
        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f],f))

        topk = list()
        #k번 만큼 추출, 최소 힙 (Min Heap)이므로 가장 작은 음수 순으로 추출

        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])

        return topK


# # # # # # # # # # # # # # # # # # # # # most_common 활용. 파이썬다운 풀이.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return list(zip(*collections.Counter(nums).most_common(k)))[0]
