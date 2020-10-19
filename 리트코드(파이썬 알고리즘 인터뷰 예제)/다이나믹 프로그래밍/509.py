#피보나치 수

#풀이 방법

'''
피보나치 수는 다이나믹 프로그래밍 대표 문제로
코딩인터뷰에서 단골문제다.
잘 알아둬야 한다.

1.하향식 풀이 : 메모이제이션
2.상향식 풀이 : 타뷸레이션
'''

# # # # # # # # # # # # # # # # # # # # # 메모이제이션
'''
재귀로 계산해 나가지만, 이미 계산한 값은 저장해뒀다가 바로 리턴한다.
'''
class Solution:

    dp=collections.defaultdict(int)

    def fib(self, N: int) -> int:
        if N <= 1:
            return N;

        if self.dp[N]:
            return self.dp[N];
        self.dp[N] = self.fib(N-1) + self.fib(N-2)
        return self.dp[N]


# # # # # # # # # # # # # # # # # # # # # 타뷸레이션
'''
재귀 사용하지 않고 반복으로 풀이. 작은 값부터 직접 계산하면서 타뷸레이션
'''
class Solution:

    dp=collections.defaultdict(int)

    def fib(self, N: int) -> int:
        self.dp[1]=1

        for i in range(2,N+1):
            self.dp[i] = self.dp[i-1] + self.dp[i-2]
        return self.dp[N]

# # # # # # # # # # # # # # # # # # # # # 공간절약
def fib(self, N: int) -> int:
    x,y = 0,1
    for i in range(0,N):
        x,y=y,x+y
    return x
