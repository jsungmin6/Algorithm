'''
시뮬레이션하면서
max값 갱신
'''
answer = 0
total = 0
for _ in range(10):
    o, i = map(int, input().split())
    total -= o
    total += i
    answer = max(answer, total)

print(answer)
