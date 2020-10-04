#중복 문자 제거

'''
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/



Example 1:

Input: s = "cdadabcc"
Output: "adbc"
Example 2:

Input: s = "abcd"
Output: "abcd"
Example 3:

Input: s = "ecbacba"
Output: "eacb"
Example 4:

Input: s = "leetcode"
Output: "letcod"


Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
'''

#풀이 방법

'''
1.재귀함수호출
2.스택구조이용
'''

# # # # # # # # # # # # # # # # # # # # # 재귀함수
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        #집합으로 정렬
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            #전체 집합과 접미사 집합이 일치할 때 분리 진행
            if set(s) == set(suffix):
                return char + selt.removeDuplicateLetters(suffix.replace(char,''))
        return ''


# # # # # # # # # # # # # # # # # # # # # 스택
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = collections.Counter(s), set(), []
        for char in s:
            counter[char] -=1
            if char in seen:
                continue
            #뒤에 붙일 문자가 남아 있다면 스택에서 제거
            while stack and char<stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return ''.join(stack)
