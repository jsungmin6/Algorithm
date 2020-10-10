#용액

#풀이방법
'''
양쪽 끝에 포인터를 두고 진행하면 될듯 싶다. 0이 나오면 출력
제일 큰 수, 작은 수가 아니라 0에 가까운 수가 정답이기 때문에 절대값을 사용해서 비교
sum과 sum_min을 비교하다가 제일 작은 sum이 나오면 sum_min에 저장되기에 그때 조건문을 이용해서 데이터를 갱신
합이 0이 나오면 바로 출력하고 종료
'''

# # # # # # # # # # # # # # # # # # # # # # # # # # #
import sys
input = sys.stdin.readline

N=int(input())
data_list=list(map(int,input().split()))

left=0
right=len(data_list)-1
sum_min=sys.maxsize

while left<right:
    sum=data_list[left]+data_list[right]
    sum_min=min(abs(sum_min),abs(sum))

    if sum_min==abs(sum):
        left_data=data_list[left]
        right_data=data_list[right]

    if sum>0:
        right-=1
    elif sum <0:
        left+=1
    else:
        print(data_list[left],data_list[right])
        exit(0) #백준은 exit(0)에 0이 아닌 다른 숫자가 오면 런타임 에러가 생김.

print(left_data,right_data)
# # # # # # # # # # # # # # # # # # # # # # # # # # # 다른사람풀이
'''
같은 방식인데 함수로 감싸ㅓ 좀 더 깔끔함.
'''
import sys
def solution(liq):
    l=0
    r=len(liq)-1
    ans = [abs(liq[l]+liq[r]),(liq[l],liq[r])]

    while l<r:
        mix = liq[l]+liq[r]
        if abs(mix) < ans[0]:
            ans[0] = abs(mix)
            ans[1] = (liq[l],liq[r])
        if mix > 0:
            r-=1
        elif mix < 0:
            l += 1
        else:
            return ans[1]
    return ans[1]

if __name__== "__main__":
    n = map(int,sys.stdin.readline().split())
    liq = list(map(int,sys.stdin.readline().split()))
    ans = solution(liq)
    print("{} {}".format(ans[0],ans[1]))
