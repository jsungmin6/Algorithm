#K경유지 내 가장 저렴한 항공권

#풀이 방법

'''
슬라이딩 윈도우 기법 사용, 윈도우를 진행시키면서 max값 갱신
'''

# # # # # # # # # # # # # # # # # # # # # 내 풀이
import sys
N,K=map(int,sys.stdin.readline().split())
temp_list=list(map(int,sys.stdin.readline().split()))


left=0
right=K

sum_window=sum(temp_list[left:right])
max_sum=sum_window

while right<N:
    sum_window-=temp_list[left]
    left+=1
    right+=1
    sum_window+=temp_list[right-1]
    max_sum=max(max_sum,sum_window)

print(max_sum)


# # # # # # # # # # # # # # # # # # # # # 다른 사람 풀이

N, M = map(int, input().split())

Temperatures = list(map(int, input().split()))

Result = []
for idx in range(N-M+1) :
    Result.append(sum(Temperatures[idx:idx+M]))

print(max(Result))
