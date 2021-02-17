'''
풀이
이중 포문으로 모든 수를 비교해야 할 듯 => 시간초과

정렬 후 투포인터로 풀어보자 시작지점을 양 끝으로 한다.
'''
##투포인터

n = int(input())
arr = list(map(int,input().split()))
arr.sort()

x = int(input())
answer=0
s,e = 0,n-1

while s<e:
    total = arr[s] + arr[e]
    if total < x:
        s+=1
    if total > x:
        e-=1
    if total == x:
        answer+=1
        s+=1

print(answer)

# #시간초과 2중포문
# n = int(input())
# arr = list(map(int,input().split()))
# arr.sort()

# x = int(input())
# answer=0
# flag=False
# for i in range(n):
#     for j in range(i+1,n):
#         total = arr[i] + arr[j]
#         if total > x:
#             if j == i+1:
#                 flag=True
#             break
#         if total == x:
#             answer+=1
#     if flag:
#         break

# print(answer)