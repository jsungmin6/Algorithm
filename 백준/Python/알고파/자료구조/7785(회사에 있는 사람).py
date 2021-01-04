import sys
input = sys.stdin.readline

N=int(input())
enter_list={}
for _ in range(N):
    name,status = input().rstrip().split()
    if status == 'enter':
        enter_list[name]=1
    else:
        enter_list[name]=0

e=sorted(enter_list.items(),reverse=True)

for n,s in e:
    if s==1:
        print(n)