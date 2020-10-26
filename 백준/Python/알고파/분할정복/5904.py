#복제 로봇

#풀이 방법

'''
1.분할 정복
2.N 개 될때까지 문장 만들고 출력 => 메모리초과

1.숫자를 먼저 구하고
2.index를 추적해보자
'''

import sys
input=sys.stdin.readline
N=int(input())
limit=1000000000
S=[3]
o_num=4
i=0
while True:
    temp=S[i]*2+o_num;
    if temp>limit:
        break
    S.append(temp)
    i+=1
    o_num+=1
print(S)



# # # # # # # # # # # # # # # # # # # # 메모리 초과 풀이
# import sys
# input=sys.stdin.readline
# N=int(input())
#
# S='moo'
# o_num=3
# while True:
#     str = S + 'm' + 'o'*o_num + S;
#     print(str)
#     if len(str) >= N:
#         print(str[N-1])
#         break
#     else:
#         S=str;
