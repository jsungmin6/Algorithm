# 박스 채우기

'''
큰 박스 부터 채워나가면서 다음 박스가 몇개 필요한지 계산한다.
'''


import sys
import heapq
input = sys.stdin.readline
length, width, height = map(int,input().split())
N = int(input())
boxs = sorted([list(map(int,input().split())) for _ in range(N)],reverse = True)

need_boxs=[]
before=0
before_num=0
for j,box in enumerate(boxs):
    i, n = box
    box_len = 2**i
    num = (length//box_len)*(width//box_len)*(height//box_len)
    num = num-before_num # 지금까지 전에 사용한 박스 공간만끔 빼줌 = 현재시점에서 필요한 박스의 수 
    before = min(n,num) # 사용할 박스의 수
    before_num = before*8 + before_num*8 # 다음 박스 크기에서 전에 사용한던 박스공간 계산

    need_boxs.append(before) # 사용한 박스의 수 보관

    if j == len(boxs)-1: # 제일 작은 박스에서 필요한 박스의 수보다 공급하는 박스의 수가 적으면 공간을 채울 수 없다.
        if n<num:
            print(-1)
            exit(0)

print(sum(need_boxs))





