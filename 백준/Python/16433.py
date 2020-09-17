N,R,C=map(int,input().split())

if (R+C)%2 == 1 :
    for i in range(N):
        for j in range(N):
            if (i+j)%2 == 1:
                print('v',end='')
            else:
                print('.',end='')
        print()
else:
    for i in range(N):
        for j in range(N):
            if (i+j)%2 == 0:
                print('v',end='')
            else:
                print('.',end='')
        print()

n,r,c=map(int,input().split())
for y in range(n):
    print(*['v'if(x%2^y%2)==(r%2^c%2)else'.'for x in range(n)],sep='')
