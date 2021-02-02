'''
피보나치 음수 확장
음수규칙보면 절대값이 짝수일때만 음수인 피보나치 수이다.
'''

N=int(input())

a=0
b=1
for i in range(abs(N)-1):
    a,b = b%1000000000,(a+b)%1000000000;

if N<0 and N%2 == 0:
    print(-1)
elif N==0:
    print(0)
    print(0)
    exit()
else:
    print(1)

print(b%1000000000)



