from math import gcd
N=int(input())
for _ in range(N):
    s = input()
    if '(' not in s:
        a=int(s[2:])
        b=10**len(s[2:])
        temp=gcd(a,b)
        a=a//temp
        b=b//temp
        print('{0}/{1}'.format(a,b))
    elif s[2] == '(':
        a=int(s[3:-1])
        b=int('9'*len(s[3:-1]))
        temp=gcd(a,b)
        a=a//temp
        b=b//temp
        print('{0}/{1}'.format(a,b))
    else:
        x,y=s[2:].split('(')
        y=y[:-1]
        a=int(x+y)-int(x)
        b=int('9'*len(y)+'0'*len(x))
        temp=gcd(a,b)
        a=a//temp
        b=b//temp
        print('{0}/{1}'.format(a,b))
