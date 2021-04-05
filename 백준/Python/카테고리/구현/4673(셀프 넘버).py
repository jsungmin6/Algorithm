'''
1부터 수를 증가시켜가면서 10000까지 d(n)을 계속해서 적용시켜나가면서 수를 제외한 다음 남은 수를 출력
'''


nums = [0]*10001

for i in range(1,10000):
    target = i
    if nums[target]:
        continue
    while target <= 10000:
        target = target + sum(list(map(int,list(str(target)))))
        if target > 10000 or nums[target]:
            break
        nums[target] = 1

for i in range(1,10001):
    if not nums[i]:
        print(i)