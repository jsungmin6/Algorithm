'''
[풀이]
dfs 인데 경로를 저장하고 경로방문을 작은 수부터 한다.
'''
import sys
input = sys.stdin.readline

def combi(n,j,prev):
    global lotto,k
    # print("n:",n)
    if n == 6:
        print(*prev)
        return

    for i in range(j+1,k):
        prev.append(lotto[i])
        combi(n+1,i,prev)
        prev.pop()


while True:
    S = list(map(int,input().split()))
    if len(S) == 1:
        break
    k = S[0]
    # print("k:",k)
    lotto = S[1:]
    combi(0,-1,[])
    print()
    