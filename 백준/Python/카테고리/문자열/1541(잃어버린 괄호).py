'''
풀이
초기 숫자 : 첫 뺄셈이 나올때까지의 합
뺄셈 뒤에나온건 어차피 다 묶여서 뺄셈이 된다.
'''
import re
S = input()
pm = []
for i in S:
    if i == '+' or i == '-':
        pm.append(i)

nums = list(map(int,(re.split('[+-]', S))))

if not '-' in pm:
    print(sum(nums))
    exit()

idx = pm.index('-')+1

print(sum(nums[:idx])-sum(nums[idx:]))


###깔끔한 풀이
import sys

input = sys.stdin.readline

arr = input().split('-')
s = 0
for i in arr[0].split('+'):
    s += int(i)
for i in arr[1:]:
    for j in i.split('+'):
        s -= int(j)
print(s)