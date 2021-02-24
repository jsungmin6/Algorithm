'''
풀이
1.산술평균 : 산술평균 다 더한 후 N으로 나눔 => 파이썬 반올림 주의 (0.5 더하구 내림 사용)
2.중아값 정렬후  N//2 값
3.최빈값: Counter, sort 사용
4.범위 : max-min 
'''
from collections import Counter
import math
import sys
input = sys.stdin.readline
N= int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

#산술평균
a=math.floor(sum(nums)/N + 0.5)
print(a)
#중앙값
nums.sort()
b=nums[N//2]
print(b)
#최빈값
cnt = Counter(nums).most_common()
# print(cnt)
if len(cnt) == 1:
    print(cnt[0][0])
elif cnt[0][1] == cnt[1][1]:
    cnt.sort(key= lambda x:(-x[1],x[0]))
    print(cnt[1][0])
else:
    print(cnt[0][0])
#범위
d = nums[-1]-nums[0]
print(d)
