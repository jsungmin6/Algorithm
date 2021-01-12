import sys
input = sys.stdin.readline
print = sys.stdout.write

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()


def dfs(cnt, row):
    if cnt == M:
        print(*row)
        return
    for i in range(N):
        row.append(nums[i])
        dfs(cnt + 1, row)
        row.pop()


for j in range(N):
    dfs(1, [nums[j]])

#신박한 라이브러리
# import sys
# input = sys.stdin.readline
# print = sys.stdout.write
# from itertools import product

# def BOJ_15656():
#     n,m = map(int,input().split())
#     arr = list(map(int,input().split()))
#     arr.sort()
#     arr = [str(i) for i in arr]
#     p = product(arr, repeat=m)
#     print("\n".join(map(" ".join, p)))