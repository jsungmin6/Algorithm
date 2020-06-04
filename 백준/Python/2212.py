import sys

n=int(input())
k=int(input())

if k>=n:
    print(0)
    sys.exit()
sensor=list(map(int,input().split(' ')))
sensor.sort()

answer=[]
for i in range(1,n):
    answer.append(sensor[i]-sensor[i-1])

answer.sort(reverse=True)
for i in range(k-1):
    answer[i]=0

print(sum(answer))
