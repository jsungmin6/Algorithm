#조합

'''
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

You may return the answer in any order.



Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Example 2:

Input: n = 1, k = 1
Output: [[1]]
'''

#풀이 방법

'''
어떻게 이런 생각을 할 수 있는지 궁금하다.
element 배열을 만들어 append, pop 를 통해 하나씩 넣어주며
중간에 dfs 를 넣고, 파라미터를 이용해 조건을 걸어준다.
조건에 의해 k=0 이 되면 조합의 개수가 완성되었다는 것을 알려주고 element를 복사해 넣어준다.
복사하는 이유는 element를 그냥 넣게 되면, 결과 값이 추가되는 게 아니라 참조가 추가되며, 이 경우 참조된
값이 변경될 경우 같이 바뀌게 된다.
result에 element만 계속 넣는 꼴이고 마지막에 element가 [] 가 되면 안에있던 모든 element가 [] 로 변한다.

'''


# # # # # # # # # # # # # # # # # # # # # DFS 활용 풀이

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(elements,start: int,k: int):
            if k == 0:
                result.append(elements[:])

            #자신 이전의 모든 값을 고정하여 재귀호출
            for i in range(start, n+1):
                elements.append(i)
                dfs(elements,i+1,k-1)
                elements.pop()

        dfs([],1,k)
        return results

# # # # # # # # # # # # # # # # # # # # # itertools 활용 풀이
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1,n+1),k))
