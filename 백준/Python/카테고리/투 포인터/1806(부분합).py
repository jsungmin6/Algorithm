'''
풀이
연속된 수, 부분합, 자연수라는 포인트가 나왔으니 투 포인터를 사용하자.
해당하는 조건을 만들때 조건에 길이를 넣고 갱신하자

시간복잡도를 넘으니 구간합을 사용하거나 투포인터에서 sum을 사용하면 안된다.

시간 복잡도
O(N)
'''
import sys
input = sys.stdin.readline

N,S = map(int,input().split())
nums= list(map(int,input().split()))
sum_nums=[0]
t=0

for i in range(len(nums)):
    t+=nums[i]
    sum_nums.append(t)

# print("sum_nums: ",sum_nums)

s=0
e=1
max_len=100000

while True:
    if e>len(nums):
        break
    total = sum_nums[e] - sum_nums[s]
    # print("total :",total)
    # print("s,e :",s,e)
    # print("max_len :",max_len)
    if total >= S and max_len > e-s:
        max_len=e-s
        s+=1
    elif total >= S and max_len <= e-s:
        s+=1
    elif total < S:
        e+=1

if max_len == 100000:
    print(0)
else:
    print(max_len)


##이런식의 투포인터 사용도 있다. 어떻게 쓰기는 사람마다 다른 듯
N, S = map(int, input().split())
a = list(map(int, input().split()))

if sum(a)<S:
    print(0)
else:
    start = 0
    end = 0
    tmp = 0
    output = 10e+9

    for i in a:
        tmp += i
        end += 1
        while tmp >= S:
            tmp -= a[start]
            start += 1
            if end - start+1 < output:
                output = end - start+1

    print(output)