#개똥벌레

#풀이방법
'''
2차원 배열 만들고 계산해보기
배열 만들때 세로로 반전해서 쉬울 것 같다.
->메모리 초과

전체 배열을 만들지 말고 높이 배열만 만들고 바로바로 +1을 하는식으로 해보자
->시간 초과


'''

# # # # # # # # # # # # # # # # # # # # # # # # # # # 시간초과


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

# # # # # # # # # # # # # # # # # # # # # # # # # # # # 메모리초과
# import sys
# input = sys.stdin.readline
#
#
# #동굴 만들기
# N,H=map(int,input().split())
# cave=[[0]*(N+1) for i in range(H)]
# for i in range(1,N+1):
#     length=int(input())
#     if i%2==1:
#         for j in range(length):
#             cave[H-1-j][i]=1
#     else:
#         for j in range(length):
#             cave[j][i]=1
#
# sum_min=sys.maxsize
# count=1
# print(cave)
#
# #동굴 한줄씩 읽어서 최솟값과 개수 구하기
# for i in range(H):
#     sum=cave[i].count(1)
#
#     if sum==sum_min:
#         count+=1
#     else:
#         sum_min=min(sum,sum_min)
#         count=1
#
# print(sum_min,count)
