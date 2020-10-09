N=int(input())
left=0
right=1
sum=0
answer=0
while left!=right:
    for i in range(left,right):
        sum+=i;
    if sum > N:
        left+=1
    elif sum < N:
        right+=1
    else:
        left+=1
        right+=1
        answer+=1
    sum=0
print(answer)
