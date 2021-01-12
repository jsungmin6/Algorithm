import sys
input = sys.stdin.readline

N,Q = map(int,input().split())
cows=[[0,0,0]]
one=0
two=0
thr=0
for _ in range(N):
    i = int(input())
    if i == 1:
        one+=1
    elif i == 2:
        two+=1
    else:
        thr+=1
    cows.append([one,two,thr])

for _ in range(Q):
    s,e = map(int,input().split())
    temp=[]
    for i in range(3):
        diff = cows[e][i] - cows[s-1][i]
        temp.append(diff)
    print(*temp)

