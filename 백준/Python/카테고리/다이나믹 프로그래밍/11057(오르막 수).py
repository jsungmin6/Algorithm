'''
쉬운 계단 수 문제와 유사
top down 방식으로 접근
uphill(N,digit) 는 길이가 N, 첫 자릿수가 digit(0~9)인 계단 수의 개
uphill(N,0~9) 까지 더하면 답이 나온다.
'''
import sys
sys.setrecursionlimit(2000)

N=int(input())

dp=[[-1]*10 for i in range(N+1)]

def uphill(N,digit):
    if N==1:
        return 1
    if dp[N][digit]!=-1:
        return dp[N][digit]
    result=0
    for i in range(digit,10):
        result+=uphill(N-1,i)%10007
    dp[N][digit]=result%10007
    return result%10007
    
count=0
for i in range(0,10):
    count+=uphill(N,i)%10007

print(count%10007)