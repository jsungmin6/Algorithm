#두 정수의 합

#풀이 방법

'''
전가산기 구현
'''

# # # # # # # # # # # # # # # # # # # # #
class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        INT_MAX = 0x7FFFFFFF
        #합, 자릿수 처리
        while b! = 0:
            a,b = (a ^ b) & MASK, ((a&b) <<1) & MASK

        #음수처리
        if a > INT_MAX:
            a = ~(a^MASK)
        return a
