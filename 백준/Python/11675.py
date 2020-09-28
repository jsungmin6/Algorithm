# Jumbled Communication

# 풀이 과정

# 비트마스크 기법 쓰면 될 듯

#####################################

N=int(input())
data=map(int,input().split())
# for num in data:
#     for i in range(256):
#         if len(bin(i))>=10:
#             num2=int(bin(i^int(bin(i)[3:]+"0",2)),2)
#             if num2==num:
#                 print(i,end=" ")
#                 break
#         else:
#             num2=int(bin(i^int(bin(i<<1),2)),2)
#             if num2==num:
#                 print(i,end=" ")
#                 break

# for num in data:
#     for i in range(256):
#         num2=int(bin(int(bin(i^int(bin(i<<1),2)),2)&255),2)
#         if num2==num:
#             print(i,end=" ")
#             break

N=int(input())
data=map(int,input().split())

for num in data:
    for i in range(256):
        num2=int(bin((i^i<<1)&255),2)
        if num2==num:
            print(i,end=" ")
            break
