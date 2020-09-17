from math import gcd
import fractions
import copy

def solution(arr):
    def lcm(x,y):
        return x*y // gcd(x,y)

    while True:
        arr.append(lcm(arr.pop(),arr.pop()))
        if len(arr) ==1 :
            return arr[0]

data=[1]

if(len(data)==1):
    print(str(data[0])+'/'+'1')
    exit()

dataCopy= copy.deepcopy(data)
a = solution(data)

b=0
for i in dataCopy:
    b+=a//i

k = fractions.Fraction(b,a)
b = k.numerator
a = k.denominator


print(str(a)+'/'+str(b))
