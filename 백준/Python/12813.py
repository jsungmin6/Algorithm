#이진수 연산 B2

#풀이방법

#전체가 100000이라 무식하게 풀어도 될 듯.

A=input()
B=input()
str=''


for i in range(100000):
    if A[i] == B[i]:
        str=str+A[i]
    elif A[i] != B[i]:
        str=str+'0'

print(str)
str=''

for i in range(100000):
    if A[i]=='1' or B[i] == '1':
        str=str+'1'
    else:
        str=str+'0'

print(str)
str=''

for i in range(100000):
    if A[i] == B[i]:
        str=str+'0'
    elif A[i] != B[i]:
        str=str+'1'

print(str)
str=''

for i in range(100000):
    if A[i] == '0':
        str=str+'1'
    else:
        str=str+'0'

print(str)
str=''

for i in range(100000):
    if B[i] == '0':
        str=str+'1'
    else:
        str=str+'0'

print(str)
str=''
