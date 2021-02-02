'''
A,B 수는 피보나치이다.
'''


a = 1
b = 0
c = 0
d = 1

K = int(input())

for i in range(K-1):
    a,b = b,a+b
    c,d = d,c+d

print(b,d)