'''
풀이
두개로 쪼개서 합의 목록들을 구한다.
A,B배열 더한거
C,D배열 더한거
양쪽을 더해서 0이 나오는게 총합이 0인 목록이다.
'''
import sys
input = sys.stdin.readline

n = int(input())
A,B,C,D = [],[],[],[]
for i in range(n):
    a,b,c,d = map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

ab,cd= {},{}
for a in A:
    for b in B:
        if ab.get(a+b):
            ab[a+b] +=1
        else:
            ab[a+b] = 1

for c in C:
    for d in D:
        if cd.get(c+d):
            cd[c+d] +=1
        else:
            cd[c+d] = 1

# cnt = 0
# for key,value in ab.items():
#     if cd.get(-key):
#         cnt += value * cd[-key]

ans = 0 
for _, key in enumerate(ab):
    if cd.get(-key):
        ans += (ab[key] * cd[-key])

print(ans)