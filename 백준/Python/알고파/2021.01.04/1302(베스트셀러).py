
import sys
input = sys.stdin.readline
N = int(input())
sells = dict()

for _ in range(N) :
    book = input().rstrip()
    if book in sells :
        sells[book] += 1
    else :
        sells[book] = 1

print(sorted(sells.items(), key=lambda x: (-x[1],x[0]))[0][0])


