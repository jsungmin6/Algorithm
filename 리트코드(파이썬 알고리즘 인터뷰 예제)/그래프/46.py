#전화번호 문자 조합

'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''

#풀이 방법

'''
for으로 남는거에서 하나씩 붙여주면서 dfs 실행
'''


# # # # # # # # # # # # # # # # # # # # # DFS 활용 풀이

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        prev_elements=[]

        def dfs(elements):
            #리프 노드일 때 결과 추가
            if len(elements) = 0:
                result.apend(prev_elements[:])

            #순열 생성 재귀 호출
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return results

# # # # # # # # # # # # # # # # # # # # # DFS 활용 풀이
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))
