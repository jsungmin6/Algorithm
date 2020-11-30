'''
top down 방식으로 접근
stair(N,digit) 는 길이가 N, 첫 자릿수가 digit(0~9)인 계단 수의 개
stair(N,1~9) 까지 더하면 답이 나온다.
N을 top down 방식으로 줄여나가며 N=1 일때 1을 리턴하도록 함
stair(N,digit)=stair(N-1,digit+1)+stait(N-1,digit-1)임을 이용
구한것을 또 구하지 않기 위해 dp배열을 만들어 결과값을 저장하면서 진행.
'''
import sys
sys.setrecursionlimit(1000)

N=int(input())

dp=[[0]*10 for i in range(N+1)]

def stair(N,digit):
    if N==1:
        return 1
    if dp[N][digit]!=0:
        return dp[N][digit]
    if digit == 0:
        result = stair(N-1,digit+1)%1000000000
        dp[N][digit]=result
        return result
    if digit == 9:
        result = stair(N-1,digit-1)%1000000000
        dp[N][digit]=result
        return result
    if digit != 0 and digit != 9:
        result = (stair(N-1,digit+1)%1000000000+stair(N-1,digit-1)%1000000000)%1000000000
        dp[N][digit]=result
        return result
    
count=0
for i in range(1,10):
    count+=stair(N,i)%1000000000

print(count%1000000000)