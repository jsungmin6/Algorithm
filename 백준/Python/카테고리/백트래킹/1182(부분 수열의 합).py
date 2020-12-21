N, S = map(int, input().split())
nums = list(map(int, input().split()))
count = 0
total = 0

def dfs(i):
    global count
    global total
    # return조건
    if i == N:
        return

    if total + nums[i] == S:
        count += 1

    # 해당 원소를 추가하지 않음
    dfs(i+1)

    # 해당 원소를 추가
    total += nums[i]
    dfs(i+1)

    total -= nums[i]

dfs(0)
print(count)
