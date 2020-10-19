#계단 오르기

#풀이 방법

'''
다이나믹 프로그래밍
피보나치 수열
'''

# # # # # # # # # # # # # # # # # # # # #


class Solution:
    dp = collections.defaultdict(int)
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n;

        if self.dp[n]:
            return self.dp[n]
        self.dp[n]=self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dp[n]
