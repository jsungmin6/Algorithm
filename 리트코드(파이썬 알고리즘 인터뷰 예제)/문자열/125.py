#125. Valid Palindrome

'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
'''

#풀이 방법

'''
1.리스트로 변환해서 양쪽에서 하나씩 비교해가며 팰린드롬 판별
2.Deque를 활용해 좀 더 시간 줄임
3.슬라이싱 [::-1] 활용
시간사용 1>2>3
'''

s="A man, a plan, a canal: Panama"

from collections import Deque

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs=[]
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs)>1:
            if strs.pop() != strs.pop(0):
                return False;

        return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs: Deque = deque()
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs)>1:
            if strs.popleft() != strs.pop():
                return False;

        return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()

        s=re.sub('[^a-z0-9]','',s)

        return s == s[::-1]
