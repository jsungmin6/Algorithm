'''
피보나치
'''

N=int(input())

a=0
b=1
for i in range(N+1):
    a,b=b,a+b
print(b*2)

