#폰트

#문제해결

#모든조합 해봐야 함.
#모든조합 for 문 돌리며 set 차집합으로 없어지는지 체크

########################################

from itertools import combinations

N=int(input())
items=[]
R=list('abcdefghijklmnopqrstuvwxyz')
R=set(R)
for _ in range(N):
    items.append(input())

data=[]
count=0
for k in range(1, len(items)+1):
    for i in list(map(''.join,combinations(items, k))):
        answer=R-set(list(i))
        if list(answer)==[]:
            count+=1


print(count)
