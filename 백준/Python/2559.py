#수들의 합 2

#풀이방법
#슬라이딩 윈도우

N,M = map(int,input().split())
array=list(map(int,input().split()))

# sumList=[0]
# sum=0
# for i in array:
#     sum+=i
#     sumList.append(sum)

left=0
right=M-1
maxAnswer=0

sum_value=0
for i in range(right+1):
    sum_value+=array[i]
maxAnswer=sum_value
while right<N-1:
    left+=1
    right+=1
    sum_value-=array[left-1]
    sum_value += array[right]
    maxAnswer=max(maxAnswer,sum_value)
print(maxAnswer)
