'''
풀이
increase[i] = i번째까지 최대 증가하는 수열 길이
decrease[i] = i번째~마지막까지 최대 감소하는 수열 길이
'''

N = int(input())
arr = list(map(int,input().split()))
increase = [1]*N
decrease = [1]*N
for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            increase[i] = max(increase[i],increase[j]+1)

print(increase)
rev_arr = arr[::-1]

for i in range(N):
    for j in range(i):
        if rev_arr[i] > rev_arr[j]:
            decrease[i] = max(decrease[i],decrease[j]+1)

decrease =decrease[::-1]

answer = 0
print(decrease)

for i in range(N):
    answer = max(answer, decrease[i]+increase[i])

print(answer-1)