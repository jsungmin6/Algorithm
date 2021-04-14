'''
풀이
이분탐색
'''

X,Y = map(int,input().split())
Z = Y*100//X

print("Z : ",Z)
if Z >= 99:
    print(-1)
    exit()

lo = 0
hi = 1000000000

while lo+1 < hi:
    mid = (lo+hi)//2
    result = (Y+mid)*100//(X+mid)
    print("hi : ",hi)
    print("lo : ",lo)
    print("mid : ",mid)
    print("result : ",result)
    if result - Z >= 1:
        hi = mid
    elif result - Z < 1:
        lo = mid




print(hi)




#부르트 포스 -> 시간초과
# X,Y = map(int,input().split())
# Z = Y*100//X
# answer = Z
# cnt = 0
# while answer == Z:
#     Y+=1
#     X+=1
#     cnt+=1
#     answer = Y*100//X
#     if answer == 100:
#         cnt = -1
#         break
# print(cnt)


