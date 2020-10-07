#부분 집합

'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''

#풀이 방법

'''
itertools.combinations 사용
combination을 리스트로 바꾸기 좀 까다로왔 음
'''


# # # # # # # # # # # # # # # # # # # # # 내 풀이
from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer =[[]]
        for r in range(1,len(nums)+1):
            for x in combinations(nums, r):
                data=list(x)
                answer.append(data)
        return answer

# # # # # # # # # # # # # # # # # # # # # 책 풀이 dfs 활용

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def dfs(index,path):
            #매번 결과 추가
            result.append(path)

            #경로를 만들면서 DFS;
            for i in range(index,len(nums)):
                dfs(i+1,path+[nums[i]])

        dfs(0,[])
        return result
