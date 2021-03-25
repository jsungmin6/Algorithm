'''
풀이
냅색dp
2차원 dp를 사용
dp[i][j] = i번 숫자를 만드는데 마지막 숫자가 j인 경우의 수
'''
import sys
input = sys.stdin.readline

T = int(input())
dp = [[0 for i in range(4)] for j in range(100001)]
mod = 1000000009

dp[1]=[0,1,0,0]
dp[2]=[0,0,1,0]
dp[3]=[0,1,1,1]

for i in range(4,100001):
    dp[i][1] = (dp[i-1][2] + dp[i-1][3]) % mod
    dp[i][2] = (dp[i-2][1] + dp[i-2][3]) % mod
    dp[i][3] = (dp[i-3][1] + dp[i-3][2]) % mod


for _ in range(T):
    print(sum(dp[int(input())]) % mod)


#다른 풀이
'''
end1[i] = i번째수가 1로 끝나는 경우의 수
end2[i] = i번째수가 2로 끝나는 경우의 수
'''

import sys
 
input = sys.stdin.readline
flush = sys.stdout.flush

end1 = [None, 1, 0, 1]
end2 = [None, 0, 1, 1]
end3 = [None, 0, 0, 1]
for _ in range(10**5):
    tmp1 = end2[-1] + end3[-1]
    tmp2 = end1[-2] + end3[-2]
    tmp3 = end1[-3] + end2[-3]
    end1.append(tmp1 % (10**9 + 9))
    end2.append(tmp2 % (10**9 + 9))
    end3.append(tmp3 % (10**9 + 9))

for _ in range(int(input())):
    n = int(input())
    print((end1[n] + end2[n] + end3[n]) % (10**9 + 9))
