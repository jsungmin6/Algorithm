'''
[풀이]
비트마스킹 으로 풀어보자
'''
import sys
input = sys.stdin.readline

a,b = int(input(),2), int(input(),2)
n = 100000
mask = 2 ** n - 1

print(f'{a&b:0{n}b}') # 자리수는 총 10만 자리 인데 빈자리는 0을 채우고 나머지는 a&b를 채우는데 그걸 2진수로 표현
print(f'{a|b:0{n}b}')
print(f'{a^b:0{n}b}')
print(f'{mask-a:0{n}b}')
print(f'{mask-b:0{n}b}')
