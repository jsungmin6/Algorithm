#조합의 합

'''
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.



Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []
Example 4:

Input: candidates = [1], target = 1
Output: [[1]]
Example 5:

Input: candidates = [1], target = 2
Output: [[1,1]]


Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500
'''

#풀이 방법

'''
dfs 를 이용해서 풀 수 있을 것 같다.
'''


# # # # # # # # # # # # # # # # # # # # # 내 풀이

candidtaes_num=len(candidates)
sum_list=[]
answer=[]

def dfs(sum_list,start):
    total=sum(sum_list)
    if total > target:
        return;
    elif total < target:
        for i in range(start,candidtaes_num):
            sum_list.append(candidates[i])
            dfs(sum_list,i)
            sum_list.pop()
    else:
        answer.append(sum_list[:])
dfs([],0)
print(answer)

# # # # # # # # # # # # # # # # # # # # # 책 풀이

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]

        def dfs(csum, index, path):
            #종료조건
            if csum <0:
                return;
            if csum ==0:
                result.append(path)
                return;

            #자기 자신부터 원소 하위까지의 나열 재귀 호출
            for i in range(index,len(candidates)):
                dfs(csum-candidates[i],i,path+[candidates[i]])

        dfs(target,0,[])
        return result
