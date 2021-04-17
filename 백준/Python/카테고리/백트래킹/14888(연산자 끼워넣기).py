'''
풀이
모든 경우를 탐색해야 한다.
'''
#백트래킹 코드
N = int(input())
nums = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_, max_ = 1e9, -1e9

def dfs(i, res, add, sub, mul, div):
    global max_, min_
    if i == N:
        max_ = max(res, max_)
        min_ = min(res, min_)
        return

    else:
        if add:
            dfs(i+1, res+nums[i], add-1, sub, mul, div)
        if sub:
            dfs(i+1, res-nums[i], add, sub-1, mul, div)
        if mul:
            dfs(i+1, res*nums[i], add, sub, mul-1, div)
        if div:
            dfs(i+1, int(res/nums[i]), add, sub, mul, div-1)

dfs(1, nums[0], add, sub, mul, div)
print(max_)
print(min_)

# 시관초과 permutations 사용 코드
# from itertools import permutations

# N = int(input())
# arr = list(map(int,input().split()))
# data = list(map(int,input().split()))
# data_li = []
# for i,d in enumerate(data):
#     for j in range(d):
#         data_li.append(i)

# permus = permutations(data_li,N-1)
# min_ans=1000000000
# max_ans=-1000000000
# for permu in permus:
#     result = arr[0]
#     for i,d in enumerate(permu):
#         if d==0:
#             result+=arr[i+1]
#         elif d==1:
#             result-=arr[i+1]
#         elif d==2:
#             result*=arr[i+1]
#         else:
#             if result < 0:
#                 result = ((result*(-1))//arr[i+1])*(-1)
#             else:
#                 result//=arr[i+1]
#     min_ans=min(min_ans,result)
#     max_ans=max(max_ans,result)

# print(max_ans,min_ans)


