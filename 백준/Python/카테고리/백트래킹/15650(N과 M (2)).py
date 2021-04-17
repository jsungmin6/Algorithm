'''
풀이
조합을 구하라
'''

N,M= map(int,input().split())
def back(idx,prev):
    if M-len(prev) > N-idx:
        return
    if len(prev) == M:
        print(*prev)
    
    for i in range(idx+1,N+1):
        prev.append(i)
        back(i,prev)
        prev.pop()

back(0,[])