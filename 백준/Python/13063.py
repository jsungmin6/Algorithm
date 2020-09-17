data=['8 3 3','12 4 6','7 4 3','7 5 1','0 0 0']


i=0
while True:
    n,m,k=map(int,data[i].split())

    if n==0 and m==0 and k==0:
        break


    if k*2>=n:
        print(-1)
    elif m>=(n//2)+1:
        print(0)
    else:
        print((n//2)+1-m)

    i=i+1
