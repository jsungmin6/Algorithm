'''
풀이
좌표 x,y가 1을 제외한 공약수가 있으면 겹친다.
'''
import sys
from math import gcd
input = sys.stdin.readline

C=int(input())
arr=[]
for _ in range(C):
    arr.append(int(input()))

N = max(arr)
Map=[[0 for i in range(1001)] for j in range(1001)]
Map[1][0],Map[0][1],Map[1][1]=1,1,1
line=0
for i in range(2,1001):
    for j in range(1,1001):
        if gcd(i,j) > 1 and j!=1:
            continue
        Map[i][j],Map[j][i] = 1,1
    
for i in arr:
    answer=0
    for j in range(i+1):
        # print(Map[j][:i+1])
        answer+=sum(Map[j][:i+1])
    print(answer)
