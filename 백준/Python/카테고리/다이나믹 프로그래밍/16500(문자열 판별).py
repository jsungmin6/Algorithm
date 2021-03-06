'''
word(k) k는 남아있는 문자. 후보 문자열로 k를 만들 수 있으면 1 리턴 없으면 0리턴
'''

S = input()
N = int(input())
A = []

for _ in range(N):
    A.append(input())

ch = False

dp=[0]*(len(S)+1)

def word(k):
    global ch
    if len(k) == 0:
        ch = True
        return ch
    if dp[len(S)-len(k)] == 1:
        return 
    for a in A:
        a_l = len(a)
        if len(k) < a_l:
            continue
        if k[0:a_l] == a:
            dp[len(S)-len(k)] = 1
            word(k[a_l:])
    return ch

word(S)

if ch:
    print(1)
else:
    print(0)
