#125. 문자열 뒤집기

'''
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.



Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
'''

#풀이 방법

'''
1.투포인터
2.reverse() 사용
3.s[::-1] 사용
'''

class Solution:
    def reverseString(self, s: List[str]) -> None:
        left,right = 0, len(right)-1
        while left<right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[::-1]
