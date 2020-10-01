#자신을 제외한 배열의 곱

'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).
나눗셈을 하지 말고 O(n)에 풀이.

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

'''

#풀이 방법

'''
1.큰수끼리 min 해야 그나마 큰 수 남을 듯
2.sort 해서 두개씩 짝지어서 min 연산하고 결과값 더하면 될 듯
'''

# 내 풀이 # # # # # # # # # # # # #

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out=[]
        p=1
        #왼쪽 수 곱하기
        for i in range(len(nums)):
            out.append(p)
            p=p*nums[i]

        p=1
        #오른쪽 수 곱하기
        for i in range(len(nums)-1,0-1,-1):
            out[i]=out[i]*p
            p=p*nums[i]
        return out
