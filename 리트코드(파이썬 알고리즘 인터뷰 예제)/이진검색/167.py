#두 수의 합2

#풀이 방법

'''
투포인터(효율좋음)
이진검색
bisect 모듈 + 슬라이싱 : 슬라이싱으로 인해 속도 느려짐
bisect 모듈 + 슬라이싱 최소화 : 슬라이싱 최소화 해서 개선
bisect 모듈 + 슬라이싱 제거 : 슬라이싱 대대신 bisect.bisect_left(a,x,lo=0) 3번째 파라미터 사용. 몇번째 인덱스부터 찾을건지 설정
투포인터와 슬라이싱 제거 제일 빠르다.

'''

# # # # # # # # # # # # # # # # # # # # # 투포인터
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right = 0, len(number) -1
        while not left == right:
            if numbers[left] + numbers[right] < target:
                left +=1
            elif numbers[left] + numbers[right] > target:
                right +=1
            else:
                return left +1,right+1

# # # # # # # # # # # # # # # # # # # # # 이진검색
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            left, right = k+1, len(numbers)-1
            expected = target - v
            #이진 검색으로 나머지 값 판별
            while left <= right:
                mid = left + (right -left)//2
                if numbers[mid] < expected:
                    left = mid +1
                elif numbers[mid] > expected:
                    right = mid -1
                else:
                    return k+1,mid+1

# # # # # # # # # # # # # # # # # # # # # bisect 모듈 + 슬라이싱
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers[k+1:],expected)
            if i < len(numbers[k+1:]) and numbers[i+k+1] == expected:
                return k+1, i+k+2

# # # # # # # # # # # # # # # # # # # # # bisect 모듈 + 슬라이싱 최소화
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            nums=numbers[k+1:]
            i = bisect.bisect_left(nums,expected)
            if i < len(nums) and numbers[i+k+1] == expected:
                return k+1, i+k+2

# # # # # # # # # # # # # # # # # # # # # bisect 모듈 + 슬라이싱 제거
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers,expected,k+1)
            if i < len(numbers) and numbers[i] == expected:
                return k+1, i+1
