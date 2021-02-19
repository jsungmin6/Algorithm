'''
풀이
정렬 sort()사용

'''

import sys
input = sys.stdin.readline

N=int(input())
slist = set()
for _ in range(N):
    s = input().rstrip()
    slist.add(s)

slist = list(slist)
slist.sort(key=lambda x : (len(x),x))

for i in slist:
    print(i)