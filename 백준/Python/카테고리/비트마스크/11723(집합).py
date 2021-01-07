'''
배열로 먼저 직관적으로 풀어보겠다.
1~20이니 크기가 20인 배열을 만들고 0을 채운다
값이 들어오면 1로 바꿔준다. -> 시간초과
비트마스킹으로 풀이
'''


import sys
input = sys.stdin.readline
N=int(input())
s=0
for _ in range(N):
    data = input().rstrip().split(' ')
    if len(data) == 2:
        cmd=data[0]
        n=int(data[1])
    else:
        cmd=data[0]
    if cmd == 'add':
        s = s | (1 << n)
    elif cmd =='remove':
        s = s & ~(1 << n)
    elif cmd =='check':
        if s & (1 << n):
            print(1)
        else:
            print(0)
    elif cmd =='toggle':
        s = s ^ (1 << n)
    elif cmd == 'all':
        s=2**21-1
    else: # empty:
        s=0

# import sys
# input = sys.stdin.readline
# N=int(input())
# s=[0]*21
# for _ in range(N):
#     data = input().rstrip().split(' ')
#     if len(data) == 2:
#         cmd=data[0]
#         n=int(data[1])
#     else:
#         cmd=data[0]
#     if cmd == 'add':
#         s[n] = 1
#     elif cmd =='remove':
#         s[n] = 0
#     elif cmd =='check':
#         if s[n]:
#             print(1)
#         else:
#             print(0)
#     elif cmd =='toggle':
#         if s[n]:
#             s[n]=0
#         else:
#             s[n]=1
#     elif cmd == 'all':
#         for i in range(1,21):
#             s[i]=1
#     else: # empty:
#         for i in range(1,21):
#             s[i]=0