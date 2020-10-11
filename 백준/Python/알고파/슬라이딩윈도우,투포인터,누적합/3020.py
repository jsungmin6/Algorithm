#개똥벌레

#풀이 방법

'''
1.H크기의 배열을 만들어 벽을 만날 때마다 해당하는 배열인덱스에 +1 해준 후 가장 작은 인덱스를 찾음 -> 시간초과
2.종유석과 석순을 따로 생각하고 각각의 누적합을 구한 후 더해줘서 min값을 찾으려고 함 -> 비요율적으로 따로 배열을 만들어 시간초과
3.결국 블로그 참고 -> 2번 아이디어는 맞았고, 구하는 심플한 방법이 있었음.
'''

# # # # # # # # # # # # # # # # # # # # 1.
import sys
input = sys.stdin.readline
N,H=map(int,input().split())
cave=[0]*H

for i in range(1,N+1):
    length=int(input())
    if i%2==1:
        for j in range(length):
            cave[H-1-j]+=1
    else:
        for j in range(length):
            cave[j]+=1

min_line_block_num=min(cave)
min_line_count=cave.count(min_line_block_num)

print(min_line_block_num,min_line_count)

# # # # # # # # # # # # # # # # # # # # 2.

import sys
import collections
input = sys.stdin.readline
N,H=map(int,input().split())
num=[0]*H
cave=[]
for i in range(1,N+1):
    cave.append(int(input()))

cave_top=[cave[i] for i in range(len(cave)) if i%2==1]
cave_bottom=[cave[i] for i in range(len(cave)) if i%2==0]

top_sum=0
bottom_sum=0
cave_top_sum=[]
cave_bottom_sum=[]
for i in range(H):
    top_sum+=collections.Counter(cave_top)[H-i]
    cave_top_sum.append(top_sum)
    bottom_sum+=collections.Counter(cave_bottom)[H-i]
    cave_bottom_sum.append(bottom_sum)

total_sum=0
cave_sum=[]
for i in range(H):
    total_sum=cave_top_sum[i]+cave_bottom_sum[-i-1]
    cave_sum.append(total_sum)


cave_min=min(cave_sum)
answer=cave_sum.count(cave_min)

print(answer)

# # # # # # # # # # # # # # # # # # # # 3. 다른 사람 풀이

import sys
input = sys.stdin.readline
n, h = map(int, input().split())
# 높이가 i인 석순, 높이가 h-i+1인 종유석
cave_top = [0] * (h+1);
cave_bottom = [0] * (h+1)
for i in range(n):
    if i%2:
        cave_top[int(input())] += 1
    else:
        cave_bottom[h-int(input())+1] += 1

# 각 높이로 잘랐을 때 생기는 조각의 개수
# i줄을 잘랐을 때 석순은 높이가 i인 석순의 개수와 i+1이상의 석순의 개수

for i in range(h-1,0,-1):
    cave_top[i] += cave_top[i+1]

# i줄을 잘랐을 때 종유석의 위치가 i인 석순의 개수와 i-1이하에 위치한 종유석의 개수
for i in range(2, h+1):
    cave_bottom[i] += cave_bottom[i-1]

cave_sum = [0] * (h+1)

for i in range(1, h+1):
    cave_sum[i] = cave_top[i] + cave_bottom[i]

# 0번 인덱스 제외
cave_sum = cave_sum[1:]
cave_min_num = min(cave_sum)
print(cave_min_num, cave_sum.count(cave_min_num))
