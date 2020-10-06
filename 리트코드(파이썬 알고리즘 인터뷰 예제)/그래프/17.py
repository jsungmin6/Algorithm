#전화번호 문자 조합

'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
'''

#풀이 방법

'''
모든 조합 만드는 라이브러리 사용
'''

# # # # # # # # # # # # # # # # # # # # # 내 풀이
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        charList=[[],[],['a','b','c'],['d','e','f'],['g','h','i'],
        ['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']
        ]

        if digits =='':
            return []

        items=[]
        for i in digits:
            i=int(i)
            items.append(charList[i])

        return list(map(''.join,list(product(*items))))


# # # # # # # # # # # # # # # # # # # # # DFS 활용 풀이

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index,path):
            #끝까지 탐색하면 백트래킹
            if len(path) == len(digits):
                result.append(path)
                return;

            # 입력값 자릿수 단위 반복
            for i in range(index, len(digits)):
                #숫자에 해당하는 모든 문자열 반복
                for j in dic[digits[i]]:
                    dfs(i+1,path+j)

        #예외 처리
        if not digits:
            return []

        dic = {'2' : "abc" ....}
        result=[]
        dfs(0,"")

        return result
