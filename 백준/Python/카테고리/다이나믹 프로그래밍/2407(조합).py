'''
풀이
수학
'''

n,m = map(int,input().split())
a = 1
b = 1
k = min(m,n-m)
for i in range(k):
    a *= n-i
    b *= k-i
print(a//b)
