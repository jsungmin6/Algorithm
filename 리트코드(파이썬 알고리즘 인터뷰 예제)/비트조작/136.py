#싱글넘버

#풀이 방법

'''
0^0 =>0
4^0 =>4
4^4 =>0
두번 같은게 나오면 0으로 리셋
'''

# # # # # # # # # # # # # # # # # # # # #
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
