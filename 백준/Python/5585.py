n=int(input())

money=1000-n
array=[500,100,50,10,5,1]
k=0

for i in array:
    if money>=i:
        count=money//i
        k+=count
    money=money%i

print(k)
