'''
for문으로 돌면서 있으면 target을 바꾸는 방식으로 하면 될 것 같다.
'''

targets = ['U','C','P','C']

S = list(input())
j=0
for i in S:
    target = targets[j]
    if i == target:
        j+=1
    if j==4:
        print('I love UCPC')
        break

if j!=4:
    print('I hate UCPC')