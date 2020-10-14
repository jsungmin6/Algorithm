#해밍거리

#풀이 방법

'''
XOR 풀이
'''

# # # # # # # # # # # # # # # # # # # # #
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')
