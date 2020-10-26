#Mixing Milk

#풀이 방법

'''
구현
인덱스가 순환될 때 나누기 쓰면 좋다.
튜플로 동시에 값이 안변하고 계산 가능.
'''
# # # # # # # # # # # # # # # # # # # # # 내 풀이


import sys
input = sys.stdin.readline

C=[]
M=[]

for _ in range(3):
    c,m=map(int,input().split())
    C.append(c)
    M.append(m)

for idx in range(100):
    idx = idx%3
    next_idx = (idx+1)%3

    M[idx],M[next_idx] = max(M[idx]-(C[next_idx]-M[next_idx]),0), min(C[next_idx],M[next_idx]+M[idx])

for i in M:
    print(i)
