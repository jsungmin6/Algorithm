'''
풀이
DP와 슬라이딩 윈도우
메모리 제한이 있으니 메모리제이션 기법을 사용 못 한다.
대신 이전 배열만 기억하는 슬라이딩 윈도우 기법을 사용한다.
'''
from copy import deepcopy
import sys
input = sys.stdin.readline

N=int(input())
# temp_max=[0]*3
temp_min=[0]*3
window_min=[0]*3
window_max=[0]*3
for _ in range(N):
    temp_max = list(map(int,input().split()))
    temp_min= deepcopy(temp_max)
    for i in range(3):
        temp_max[i] += max(window_max[1], max(window_max[0],window_max[2]) if i==1 else window_max[i])
        temp_min[i] += min(window_min[1], min(window_min[0],window_min[2]) if i==1 else window_min[i])
    window_max = deepcopy(temp_max)
    window_min = deepcopy(temp_min)

print(max(window_max),min(window_min))



#### 슬라이딩 윈도우 사용 안 한 풀이

import sys
read=sys.stdin.readline

n = int(read())
a,b,c = map(int,read().split())
maxa,maxb,maxc = a,b,c
for _ in range(n-1):
    tmpa,tmpb,tmpc = map(int,read().split())
    a,b,c = tmpa + min(a,b),tmpb + min(a,b,c),tmpc + min(c,b)
    maxa,maxb,maxc = tmpa + max(maxa,maxb),tmpb + max(maxa,maxb,maxc),tmpc + max(maxc,maxb)


print(max(maxa,maxb,maxc),min(a,b,c))
