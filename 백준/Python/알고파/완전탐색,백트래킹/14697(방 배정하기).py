import sys
sys.setrecursionlimit(2000)


A,B,C,N=map(int,input().split())
visited=[]
def solution(n):
    if n > N:
        return 0
    if n == N:
        print(1)
        exit()
    if n in visited:
        return
    
    for i in [A,B,C]:
        solution(n+i)
        visited.append(n+i)

solution(0)
print(0)