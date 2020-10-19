#공항

#풀이 방법

'''
먼저 게이트 수만큼 같은 크기의 배열을 만듬
들어오는 비행기 g 범위 중 가장 큰곳이 비어있으면 넣고, 없으면 차례대로 작은 순으로 넣음
만약 넣을 곳이 없다면 중지. =>시간초과

값을 넣고, 넣은 후 왼쪽과 오른쪽 배열이 존재하면 merge한다.
값이 들어왔을 때 find 했을 때 1이 나오면 break => 구현실패

(다른사람 풀이 참조)
답 : find결과가 0 이 아니면 uf배열의 왼쪽을 오른쪽의 부모로 한다.
sys.setrecursionlimit(100000) 로 재귀스택 늘려준다.

'''



# # # # # # # # # # # # # # # # # # # # # union find 사용

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
G=int(input())
P=int(input())

uf=[i for i in range(G+1)]
num=0
airplanes=[]
for _ in range(P):
    airplanes.append(int(input()))

def find(n):
    if uf[n]==n:
        return n;
    uf[n]=find(uf[n])
    return uf[n]

for i in airplanes:
    k=find(i)
    if k==0:
        break
    uf[k]=k-1
    num+=1
print(num)

# # # # # # # # # # # # # # # # # # # # # 시간초과 풀이

# import sys
# input = sys.stdin.readline

#
# G=int(input())
# P=int(input())
#
# Gates=[-1]*(G+1)
# num=0
# airplanes=[]
# for _ in range(P):
#     airplanes.append(int(input()))
#
#
# for g in airplanes:
#     while  g>0:
#         if Gates[g]==-1:
#             num+=1
#             Gates[g]=num
#             break
#         g-=1
#     if g==0:
#         print(num)
#         break
