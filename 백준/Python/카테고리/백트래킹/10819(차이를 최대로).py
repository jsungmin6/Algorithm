'''
풀이
순열
N이 충분히 작으니 모든 경우를 해도 될 듯
'''

N = int(input())
nums = list(map(int,input().split()))
answer = 0
visited = [0]*N

def cal(arr:list):
    total = 0
    for i in range(len(arr)-1):
        total += abs(arr[i] - arr[i+1])
    return total


def f(prev):
    global answer, visited
    if len(prev) == N:
        answer = max(answer,cal(prev))
        return
    
    for i in range(0,N):
        if visited[i]:
            continue
        visited[i] =1
        prev.append(nums[i])
        f(prev)
        visited[i] = 0
        prev.pop()
f([])
print(answer)

