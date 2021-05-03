'''
풀이
LCS 를 2번 진행한다.
공통 부분 문자열 중 가장 길이가 긴 문자열을 말한다.
Subsequence : 전체 문자열에서 꼭 연속된 문자열인 것은 아닌 부분 문자열
'''


s1 = input()
s2 = input()
s3 = input()


dp = [[[0 for i in range(101)] for j in range(101)] for k in range(101)]
n1,n2,n3 = len(s1),len(s2),len(s3)

for i in range(1,n1+1):
    for j in range(1,n2+1):
        for k in range(1,n3+1):
            if s1[i-1] == s2[j-1] == s3[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] +1
            else:
                dp[i][j][k] = max(dp[i-1][j][k],dp[i][j-1][k],dp[i][j][k-1])
    

print(dp[n1][n2][n3])
