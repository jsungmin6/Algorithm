'''
풀이
'''
N,M = map(int,input().split())

def back(idx,prev):
    if len(prev) == M:
        print(*prev)
        return

    for i in range(idx,N+1):
        prev.append(i)
        back(i,prev)
        prev.pop()

back(1,[])