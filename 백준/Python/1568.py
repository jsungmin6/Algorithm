n=int(input())
fly=1
result=0

while n!=0:
    if n<fly:
        fly=1
    n-=fly
    fly+=1
    result+=1

print(result)
