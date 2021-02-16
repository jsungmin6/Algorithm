'''
풀이
1. 오름차순 정렬
2. 1번 인덱스부터 n-1번까지 arr[n]*0.9 이상인 인덱스 번호(k)와 n-k 를 누적해서 더한다. 
'''
import bisect

N = int(input())
sizeF = list(map(int,input().split()))
sizeF.sort()
answer = 0

for i in range(1,N):
    size = sizeF[i]*9/10
    idx= bisect.bisect_left(sizeF,size)
    answer += i-idx

print(answer)


#다른풀이 (슬라이딩 윈도우)
import sys
input = sys.stdin.readline

n = int(input())
num = input().split()

for i in range(n):
    num[i] = int(num[i])

num.sort()

ans = 0
left = 0
for right in range(1, n):  ## sliding widow 방식
    while left < right and num[right]*0.9 > num[left]:
        left += 1
    ans += right-left

print(ans)