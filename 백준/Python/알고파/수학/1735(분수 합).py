#주어지는 분자 분모를 우선적으로 최대공약수로 나눠 기약분수로 만들어준다.
#덧셈진행
#두 분모의 최소공배수를 구해서 덧셈 진행
#최대공약수로 다시 나눠 준다.

from math import gcd

#최소공배수
def lcm(x,y):
    return x*y//gcd(x,y)

a1,a2=map(int,input().split())
b1,b2=map(int,input().split())

temp=gcd(a1,a2)
if temp != 1:
    a1=a1//temp
    a2=a2//temp
temp=gcd(b1,b2)
if temp != 1:
    b1=b1//temp
    b2=b2//temp

lc = lcm(a2,b2)

ans1 = a1*(lc//a2) + b1*(lc//b2)
ans2 = lc

temp = gcd(ans1,ans2)
if temp != 1:
    ans1=ans1//temp
    ans2=ans2//temp
print(ans1,ans2)

#깔끔한 방법
'''
일단 덧셈 진행하고
나중에 통째로 최대공약수 나눠줌.
'''

def gcd(x, y):
    while y:
        x, y = y, x%y
    return x
a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
c, d = a1*b2+a2*b1, b1*b2
g = gcd(c, d)
print(c//g, d//g)