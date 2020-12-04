'''
맨 오른쪽 주유소는 일단 필요 없다.
주유소 start지점 보다 적은 가격의 주유소나 나올때까지의 거리의 총합 x start지점 가격이다.
작은지점에 도착하면 start지점 갱신.
반복
'''

N = int(input())
dist = list(map(int, input().split()))
costs = list(map(int, input().split()))

start = costs[0]
sum = 0
answer = 0
for i in range(1, len(costs)):
    sum += dist[i-1]
    if start <= costs[i]:
        continue
    else:
        answer += sum*start
        start = costs[i]
        sum = 0

if sum != 0:
    answer += sum*start

print(answer)
