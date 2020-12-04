
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
boxs = [list(map(int, input().split())) for i in range(n)]

Map = [[0 for i in range(m)] for i in range(n)]

for i in range(n):
    j = boxs[i].index(max(boxs[i]))
    Map[i][j] = boxs[i][j]


for j in range(m):
    min_n = 0
    index = -1
    for i in range(n):
        if min_n < boxs[i][j]:
            min_n = boxs[i][j]
            index = i
    Map[index][j] = boxs[index][j]

total = sum([sum(i) for i in boxs])
result = sum([sum(i) for i in Map])
print(total-result)
