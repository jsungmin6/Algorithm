n=int(input())
x=set(map(int,input().split()))
m=int(input())
y=list(map(int,input().split()))

for i in y:
    if(i not in x):
        print('0')
    else:
        print('1')
