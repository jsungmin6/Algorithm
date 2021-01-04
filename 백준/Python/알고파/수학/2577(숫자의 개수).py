num=1
for _ in range(3):
    num*=int(input())

num=str(num)
for i in range(10):
    cnt=0
    for j in num:
        if str(i)==j:
            cnt+=1
    print(cnt)