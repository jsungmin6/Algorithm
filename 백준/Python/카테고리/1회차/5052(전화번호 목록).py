'''
풀이
정렬후 작은 순부더 다른곳에 포함 되어있는지 확인
'''

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    phones = []
    for i in range(n):
        phones.append(input().rstrip())
    phones.sort(key=lambda x : len(x))
    ch=False

    for start in range(n-1):
        p = phones[start]
        p_l = len(p)
        for i in range(start+1,n):
            if len(phones[i]) == p_l: # 두 전화번호가 같은 경우가 없을 때가 없기 때문
                continue
            if p == phones[i][:p_l]:
                ch=True
                break
        if ch:
            break
    
    if ch:
        print('NO')
    else:
        print('YES')