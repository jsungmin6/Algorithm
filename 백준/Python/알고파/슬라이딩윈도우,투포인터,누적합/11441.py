#합 구하기

#풀이 방법

'''
누적합 배열 만들어서 뺄샘처리
'''

# # # # # # # # # # # # # # # # # # # # # 내 풀이
import sys
f=sys.stdin.readline
N=int(f())
num_list=list(map(int,f().split()))
M=int(f())

#누적합 배열
sum_list=[0]
sum=0
for i in num_list:
    sum+=i;
    sum_list.append(sum)

for _ in range(M):
    left, right = map(int,f().split())
    answer=sum_list[right]-sum_list[left-1]
    print(answer)



# # # # # # # # # # # # # # # # # # # # # 다른 사람 풀이
'''
'''
