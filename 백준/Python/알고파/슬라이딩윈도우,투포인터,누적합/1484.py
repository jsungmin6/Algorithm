#다이어트

#풀이 방법

'''
left는 1 right는 2 로 설정후 투포인터 진행.
크면 left +1 작으면 right +1 같으면 left,right,answer+1
left가 right와 같아지면 종료

'''

# # # # # # # # # # # # # # # # # # # # 내 풀이 (투 포인터)
import sys
input=sys.stdin.readline
N=int(input())

left=1
right=2
answer=[]


while left<right:
    diff=right**2 - left**2
    if diff < N:
        right+=1
    elif diff > N:
        left+=1
    else:
        answer.append(right)
        right+=1
        left+=1


if not answer:
    print(-1)
else:
    for i in answer:
        print(i)

# # # # # # # # # # # # # # # # # # # # # 다른 풀이 (수학)

'''
현재 몸무게*2 - N = 기억하는 몸무게*2

현재 몸무게 제곱근을 구했을 때 값이 자연수면 정답

'''
