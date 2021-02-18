'''
풀이
nums 배열을 만들고 숫자 개수를 센다. 9는 6에 카운팅 하고 나중에 2로 나눠준다.
가장 큰 max값이 set수 이다
'''
nums=[0]*10
for i in input():
    i=int(i)
    if i == 9:
        nums[6]+=1
    else:
        nums[i] +=1

nums[6] = (nums[6]+1)//2

print(max(nums))

