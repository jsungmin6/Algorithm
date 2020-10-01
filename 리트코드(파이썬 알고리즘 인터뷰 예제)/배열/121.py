#주식을 사고팔기 가장 좋은 시점

'''
Say you have an array for which the i element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''

#풀이 방법

'''
1.브루트 포스 방식만 생각남
2.최소값 최대값 활용
'''

# # # # # # # # # # # # # # # # # # # # #
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price=sys.maxsize

        #최솟값과 최댓값을 계속 갱신
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price-min_price)
