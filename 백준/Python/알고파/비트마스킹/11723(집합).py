'''
[풀이]
비트마스킹을 통해 풀어보자
'''
import sys
input = sys.stdin.readline

M = int(input())
bit = 0b0
n=0
for _ in range(M):
    data = input().rstrip().split(' ')
    t = data[0]
    if len(data) > 1:
        n = int(data[1])
    
    if t == "add":
        bit = bit | (1 << n)
    elif t == "remove":
        bit = bit & ~(1 << n)
    elif t == "check":
        check = bit & (1 << n)
        if check > 0 :
            print(1)
        else:
            print(0)
    elif t == "toggle":
        check = bit & (1 << n)
        if check > 0:
            bit = bit & ~(1 << n)
        else:
            bit = bit | (1 << n)
    elif t == "all":
        # bit = bin(2**21-1)
        bit = 0b111111111111111111110
    elif t == "empty":
        bit = 0b0

