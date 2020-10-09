#동전1

#풀이방법
'''

'''

# # # # # # # # # # # # # # # # # # # # # # # # # # #

import sys
input = sys.stdin.readline
N,P = map(int,input().split())
DNA=input()
A,C,G,T = map(int,input().split())

left=0
right=P
answer=0

#첫 윈도우에서 ACGT 개수 파악
window=DNA[left:right]
num_A=window.count('A')
num_C=window.count('C')
num_G=window.count('G')
num_T=window.count('T')

#첫 윈도우에서 조건 충족시 answer+=1
if num_A==A and num_C==C and num_G==G and num_T==T:
    answer+=1

#슬라이딩 윈도우 진행
while right<N:
    left_str=DNA[left]
    right_str=DNA[right]

    if left_str=='A':
        num_A-=1
    elif left_str=='C':
        num_C-=1
    elif left_str=='G':
        num_G-=1
    else:
        num_T-=1

    if right_str=='A':
        num_A+=1
    elif right_str=='C':
        num_C+=1
    elif right_str=='G':
        num_G+=1
    else:
        num_T+=1

    if num_A==A and num_C==C and num_G==G and num_T==T:
        answer+=1

    left+=1
    right+=1


print(answer)
