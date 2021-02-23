'''
풀이
'''
E,S,M = map(int,input().split())
year=1
while True:
    a =year%15
    if not a: a=15
    b= year%28
    if not b: b=28
    c= year%19
    if not c: c=19
    
    if a == E and b == S and c == M:
        print(year)
        break
    year+=1