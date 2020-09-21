#1로 만들기 s3

# 문제 해결

# 1, 2 ,3 순서대로 적용

######################

def solution(n):
    if n%3==0:
        n=n//3
    elif n%2==0:
        n=n//2
    else:
        n-=1
    return n

N=int(input())

count=0
while N!=1:
    count+=1
    N=solution(N)
    print(N)
print(count)
