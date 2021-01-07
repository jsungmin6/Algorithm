import sys
input=sys.stdin.readline

N,M = map(int,input().split())

mon_and_num={}
num_and_mon={}

for i in range(N):
    p = input().rstrip()
    mon_and_num[p] = i+1
    num_and_mon[i+1] = p

for _ in range(M):
    q=input().rstrip()
    if q.isdigit():
        print(num_and_mon.get(int(q)))
    else:
        print(mon_and_num.get(q))

