'''
풀이
lis 문제이다. 가장 길게 증가하는 부분수열을 찾으면 된다.

시간복잡도
O(N^2)
'''
import sys
input = sys.stdin.readline

N=int(input())
lines=[]
for _ in range(N):
    lines.append(list(map(int,input().split())))

lines.sort(key=lambda x : x[0])
dp=[1]*101

for i in range(N):
    for j in range(i):
        if lines[i][1] > lines[j][1]:
            dp[i]=max(dp[i],dp[j]+1)


print(N-max(dp))











##
import sys
input = sys.stdin.readline

n = int(input())
line = [list(map(int, input().split())) for _ in range(n)]
line.sort(key=lambda x: x[0])
dest = [0] * 501
for s, d in line:
    dest[d] = max(dest[:d]) + 1
    
print(n - max(dest))
