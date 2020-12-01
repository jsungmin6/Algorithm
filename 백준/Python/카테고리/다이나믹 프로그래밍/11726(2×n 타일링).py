'''
즉 홀수번째 + 짝수번째 => 다음 수 인데 
피보나치 수열이다.
'''
a=1
b=2
N=int(input())
for i in range(N-2):
    a,b= b,a+b
    a%=10007
    b%=10007

if N==1:
    print(1)
else:
    print(b)


