'''
규칙성 파악
피보나치 수열이랑 비슷함.
f(n) = 2*f(n-2) + f(n-1)
'''
a=1
b=3
N=int(input())
for i in range(N-2):
    a,b= b,a*2+b
    a%=10007
    b%=10007

if N==1:
    print(1)
else:
    print(b)


