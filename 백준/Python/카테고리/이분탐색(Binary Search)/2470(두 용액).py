'''
풀이
2개니가 조합으로 모든경우 찾아서 해보자 => 시간초과
'''

N = int(input())
arr = list(map(int,input().split()))
arr.sort()
start = 0
end = N-1
cur = 2000000001
x,y = start,end
while start < end:
    
    s = arr[start] + arr[end]

    abs_s = abs(s)
    if s > 0:
        if abs_s < cur:
            x,y = start,end
            cur = abs_s
        end-=1
    elif s < 0:
        if abs_s < cur:
            x,y = start,end
            cur = abs_s
        start+=1
    else: #s == 0
        print(arr[start],arr[end])
        break;

print(arr[x],arr[y])


#2개니까 조합으로 모든경우 찾아서 해보자
# from itertools import combinations

# N = int(input())
# arr = list(map(int,input().split()))
# combi = combinations(arr,2)
# answer = 20000000001
# ans1,ans2 = 0,0

# for a,b in combi:
#     temp = abs(a+b)
#     if temp < answer:
#         ans1 = a
#         ans2 = b
#         answer = temp

# if ans1 < ans2:
#     print(ans1,ans2)
# else:
#     print(ans2,ans1)