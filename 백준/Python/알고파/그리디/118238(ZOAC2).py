S = input()

start = 1
answer = 0
for i in S:
    i = ord(i)-64
    diff = abs(start-i)
    answer += min(diff, 26-diff)
    start = i


print(answer)
