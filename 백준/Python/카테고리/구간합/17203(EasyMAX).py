import sys
input = sys.stdin.readline

N,Q = map(int,input().split())

data = list(map(int,input().split()))

diff=[]

for i in range(1,N):
    diff.append(abs(data[i]-data[i-1]))

sums=[0]
total=0
for i in diff:
    total+=i
    sums.append(total)

for _ in range(Q):
    s,e = map(int,input().split())
    if s == e:
        print(0)
    else:
        print(sums[e-1]-sums[s-1])