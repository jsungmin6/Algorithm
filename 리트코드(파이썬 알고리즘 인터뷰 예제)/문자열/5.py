#가장 긴 팰린드롬 부분 문자열

'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''

#풀이 방법

'''
1.aa  처럼 짝수로 팰린드롬이 성립되는 경우와 aba 처럼 홀수로 팰린드롬이 성립되는 경우가 있다.
2.왼쪽부터 인덱스를 증가시켜 나가면 팰리드롬을 찾는데 위의 두가지 경우를 생각해서 2가지 경우로 나누어서 인덱스 증가를 진행시킨다.
3.짝수든 홀수는 팰린드롬수를 찾았으면 그때부터 왼쪽 오른쪽으로 팰린드롬수를 만족할 때까지 인덱스를 확장시킨다.
4.리턴한 수의 길이를 기록한다.
5.가장 긴 길이가 답이다.
'''

# # # # # # # # # # # # # #

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left,right):
            while left>=0 and right<=len(s) and s[left]==s[right-1]:
                left -=1
                right +=1
            return s[left + 1:right-1]

        if len(s)<2 or s==s[::-1]:
            return s;

        result=''
        for i in range(len(s)-1):
            result=max(result,expand(i,i+1),expand(i,i+2),key=len)

        return result
