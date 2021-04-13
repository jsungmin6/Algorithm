'''
풀이
그리디
'''

N = int(input())
P = list(map(int,input().split()))
P.sort()
total, s  = 0,0
for i in P:
    s = s + i
    total += s
print(total)
