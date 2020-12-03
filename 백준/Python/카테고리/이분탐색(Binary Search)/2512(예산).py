'''
1. 가능하면 그대로 리턴
2. 불가능 하다면 가능한 한 최대의 총 예산을 고르라.
'''

N = int(input())
needs = list(map(int,input().split()))
amt = int(input())



if sum(needs) <= amt:
    print(max(needs))
    exit()

lo = 0
hi = amt

while lo+1<hi:
    
    mid = (lo+hi)//2
    total = 0
    for i in needs:
        if mid < i:
            total += mid
        else:
            total +=i;
    # print('lo : {},hi : {}, mid : {}, total = {}'.format(lo,hi,mid,total))
    if total > amt:
        hi=mid
    else:
        lo=mid

print(lo)