'''
풀이
끝 나는 부분이 3경우로 나뉜다.
타일 1개 타일 2개 큰 타일 1개
즉 f(n)=f(n-1)+2*f(n-2) 
'''
import sys
input = sys.stdin.readline

while True:
    try:
        N=int(input())
        a=1
        b=3
        if N==0:
            print(1)
        elif N==1:
            print(1)
        else:
            for i in range(N-2):
                a,b = b,2*a+b
            print(b)
    except:
        break
    