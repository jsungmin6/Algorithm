#APC는 왜 서브태스크 대회가 되었을까?

#풀이 방법

'''
easy 문제와 hard 문제를 if elif로 구분
개수차이로 점수계산
'''
# # # # # # # # # # # # # # # # # # # # # 내 풀이
import sys
input = sys.stdin.readline
N,L,K = map(int,input().split())
easy_num=0
hard_num=0
for _ in range(N):
    easy,hard = map(int,input().split())
    if hard <= L:
        hard_num+=1
    elif easy <= L:
        easy_num+=1

answer=0
answer+=min(hard_num,K) * 140

if hard < K:
    answer+=min(easy_num,K-hard_num) * 100

print(answer)
