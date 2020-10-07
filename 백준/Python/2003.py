#수들의 합 2

#풀이방법
#투 포인터

N,M=map(int,input().split())
array=list(map(int,input().split()))
left=0
right=0
sum=0

answer=0
while right<N+1:
    for i in array[left:right]:
        sum+=i;
    if sum > M:
        left+=1
    elif sum < M:
        right+=1
    else:
        left+=1
        right+=1
        answer+=1
    sum=0
print(answer)
