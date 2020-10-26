#The candy war

#풀이 방법

'''
복잡한 구현은 함수를 나눠서 생각
1.선생님 역할
2.숫자 같아 졌는지
3.무한반복
'''
# # # # # # # # # # # # # # # # # # # # # 내 풀이
import sys
input = sys.stdin.readline

def same_candy(N:int,child:list):
    for i in range(N):
        if child[i]%2:
            child[i]+=1
    return len(set(child)) == 1

def teacher(N:int,child:list):
    temp_list=[0 for i in range(N)]
    for i in range(N):
        if child[i]%2:
            child[i]+=1
        child[i]//=2
        temp_list[(i+1)%N]=child[i]

    for i in range(N):
        child[i]+=temp_list[i]

    return child

T = int(input())
for _ in range(T):
    N=int(input())
    child=list(map(int,input().split()))
    count=0
    while not same_candy(N,child):
        count+=1
        child = teacher(N,child)
    print(count)
