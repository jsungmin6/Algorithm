#두 배열의 교집합

#풀이 방법

'''
브루트포스
하나는 정렬 하나는 이진검색
둘다 정렬 투포인터

'''

# # # # # # # # # # # # # # # # # # # # # 브루트 포스
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: set = set()
        for n1 in nums1:
            for n2 in nums2:
                if n1 == n2:
                    result.add(n1)
        return result

# # # # # # # # # # # # # # # # # # # # # 이진 검색으로 일치 여부 확인
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: set = set()
        num2.sort()
        for n1 in nums1:
            #이진 검색으로 일치 여부 판별
            i2=bisect.bisect_left(num2,n1)
            if len(num2) > 0 and len (num2) > i2 and n1 == num2[i2]:
                result.add(n1)
        return result

# # # # # # # # # # # # # # # # # # # # # 투 포인터로 일치 여부 판별
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: set = set()
        #양쪽 모두 정렬
        nums1.sort()
        nums2.sort()
        i = j = 0
        #투 포인터 우측으로 이동하며 일치 여부 판별
        while i< len(nums1) and j <len(nums2):
            if nums1[i] > nums2[j]:
                j +=1
            elif nums1[i] < nums2[j]:
                i +=1
            else:
                result.add(nums1[i])
                i+=1
                j+=1
        return result
