'''
풀이
백트래킹으로 모든 경우 탐색
'''

N,M = map(int,input().split())

def back(m,p,v):
    if len(p) == m:
        print(*p)
        return
    
    for i in range(1,N+1):
        if v[i]:
            continue
        v[i] = 1
        p.append(i)
        back(m,p,v)
        v[i] = 0
        p.pop()

prev=[]
visited = [0]*(N+1)
back(M,prev,visited)


    
    
