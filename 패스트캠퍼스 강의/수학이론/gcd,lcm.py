# 단순하게 반복문 사용
def gcd_native(a,b):
    for i in range(min(a,b),0,-1):
        if a%i == 0 and b%i == 0: return i

# 유클리드 호제법 GCD(a,b) = GCD(b,a%b)
def gcd(a,b):
    return gcd(b,a%b) if a%b!=0 else b
            
# 반복문 사용
def gcd2(a,b):
    if a%b != 0:
        a,b = b, b%a
    return b

# 라이브러리 이용
import math
math.gcd(a,b)

#최소공배수 lcm  a와 b의 최소공배수는 a*b / a 와 b의 최대공약수 이다. 
def lcm(a,b):
    a*b/gcd(a,b)
    # 다른 언어에서는 인트오버플로우 발생할 수 있으니 a/gcd(a,b) * b 가 적절하다.
