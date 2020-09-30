#두수의 합

'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''

#풀이 방법

'''
1.1층부터 올라가며 1칸 제일 작은 인덱스 1칸 제일 큰 인덱스, 2칸 제일작으 인덱스 2칸 제일 큰 인덱스 찾으며 사이 인덱스 수 구하고 채워진 인덱스는 빼서 for문 돌리려고 했으나 층수 제한이 없어 패스

2.배열을 처음부터 돌며 상승했을 때 인덱스 값을 기억, 그리고 그 다음 기억한 인덱스 값과 같은 층 or 높은 층 나오는 인덱스 기억.
3.두 기억한 인덱스 중 작은 수의 층 곱하기 사이에 있는 인덱스 개수 곱해서 사이의 총 칸 구하고, 배열에서 사이 인덱스 값 다 빼줌.
4.
'''

#스택이용한 풀이 # # # # # # # # # # # # #

height=[0,1,0,2,1,0,1,3,2,1,2,1]
stack=[]
volumn=0

for i in range(len(height)):
    while stack and height[i] > height[stack[-1]]:
        print('i : ',i,)
        print('while start :',stack)
        top = stack.pop()

        if not len(stack):
            break


        print('stack[-1] :',stack[-1])
        distance = i-stack[-1]-1
        waters = min(height[i], height[stack[-1]]) - height[top]


        volumn += distance *waters

    stack.append(i)
    print('stack :',stack)


# 투 포인터 이용 풀이 (이해감)# # # # # # # # # # # # #
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        volumn = 0
        left, right = 0, len(height)-1
        left_max, right_max = height[left],height[right]
        # 더 높은 쪽을 향해 투 포인터 이동
        while left < right:
            left_max = max(height[left],left_max)
            right_max = max(height[right],right_max)
            if left_max <= right_max:
                volumn+= left_max - height[left]
                left+=1
            else:
                volumn+= right_max - height[right]
                right-=1

        return volumn
