#중복문자 없는 가장 긴 부분 문자열

'''
Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''

#풀이 방법

'''
1.배열에 하나씩 추가하며 다음 문자가 있는지 확인하고 없으면 배열에 넣고 있으면 배열을 초기화. 배열의 max를 계속 체크
'''

# # # # # # # # # # # # # # # # # # # # # 내 풀이

data="dvdf"

array=[]
maxArray=0
for char in data:
    if not array or char not in array:
        array.append(char)
    elif char in array:
        index=array.index(char)
        array=array[(index+1):]
        array.append(char)
    maxArray=max(maxArray,len(array))

print(maxArray)

# # # # # # # # # # # # # # # # # # # # # 정답

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        max_length = start = 0
        for index, char in enumerate(s):
            # 이미 등장했던 문자라면 'start' 위치 갱신
            if char in used and start <= used[char]:
                start = used[char]+1
            else: #최대 부분 문자열 길이 갱신
                max_length = max(max_length, index - start +1)

            #현재 문자의 위치 삽입
            used[char] = index

        return max_length
