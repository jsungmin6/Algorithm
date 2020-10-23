#걸그룹 마스터 준석이

#풀이 방법

'''
브루트 포스
defaultdict사용
'''
# # # # # # # # # # # # # # # # # # # # # 내 풀이
from collections import defaultdict
import sys
input = sys.stdin.readline
N, M = map(int,input().split())
solution = defaultdict(list)
for _ in range(N):
    team_name=input()[:-1]
    member_num=int(input())
    temp=[]
    for _ in range(member_num):
        member_name=input()[:-1]
        temp.append(member_name)
    solution[team_name]=sorted(temp)

for _ in range(M):
    name=input()[:-1]
    type=int(input())

    if type == 0:
        for i in solution[name]:
            print(i)
    if type == 1:
        for key in solution.keys():
            if name in solution[key]:
                print(key)
                break;
