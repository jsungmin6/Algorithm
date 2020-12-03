'''
'''
import sys
input = sys.stdin.readline
N = int(input())
s_times =[]
e_times =[] 
for _ in range(N):
    s,e = map(int,input().split())
    s_times.append(s)
    e_times.append(e)

answer=max(s_times)-min(e_times)
if answer < 0:
    print(0)
else:
    print(answer)
    