#보석과 돌

'''
You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: J = "aA", S = "aAAbbbb"
Output: 3
Example 2:

Input: J = "z", S = "ZZ"
Output: 0
Note:

S and J will consist of letters and have length at most 50.
The characters in J are distinct.
'''

#풀이 방법

'''
1.counter 을 사용한 방식 생각
'''

# # # # # # # # # # # # # # # # # # # # #

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        freq={}
        count = 0

        #돌(S) 빈도 수 계산
        for char in S:
            if char not in freqs:
                freqs[char]=1
            else:
                freqs[char]+=1

        #보석(J)의 빈도 수 합산
        for char in J:
            if char in freqs:
                count += freqs[char]

        return count

# # # # # # # # # # # # # # # # # # # # # defaultdict 활용

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        freq=collections.defaultdict(int)
        count = 0

        #돌(S) 빈도 수 계산
        for char in S:
            freqs[char] +=1

        #보석(J)의 빈도 수 합산
        for char in J:
            count += freqs[char]

        return count

# # # # # # # # # # # # # # # # # # # # # Counter 활용

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        freq=collections.Counter(S)
        count = 0

        #보석(J)의 빈도 수 합산
        for char in J:
            count += freqs[char]

        return count

# # # # # # # # # # # # # # # # # # # # # 파이썬 다운 방식

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(s in J for s in S)
