'''
풀이
수학문제 구현
'''
A,P = map(int,input().split())
nums = []
answer = 0
target = A
while target not in nums:
    nums.append(target)
    answer+=1
    data = list(map(int,list(str(target))))
    total = 0
    for i in data:
        total+=i**P
    target = total
print(nums.index(target))