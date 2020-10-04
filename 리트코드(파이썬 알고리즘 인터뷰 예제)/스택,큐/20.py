#유효한 괄호

'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
'''

#풀이 방법

'''
1.딕셔너리에 짝 구성해놓고 스택 만들어 풀이
'''

# # # # # # # # # # # # # # # # # # # # #
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        table={
        ')':'(',
        '}':'{',
        ']':'[',
        }

        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False

        return len(stack)==0
