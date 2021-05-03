'''
풀이

플로이드 와샬

'''
from collections import defaultdict

n=5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5],[1,3]]

def solution(n, results):
    INF = 9873654321
    mat = [[0 if i==j else INF for i in range(n+1)] for j in range(n+1)]



    for result in results:
        a,b = result
        mat[a][b] = 1

    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if i==j:
                    mat[i][j] = 0
                else:
                    mat[i][j] = min(mat[i][j],mat[i][k] + mat[k][j])
    
    for i in mat:
        print(i)
    print()

    connect=[1]*(n+1)
    connect[0] = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if mat[i][j] == INF and mat[j][i] == INF:
                connect[i] = 0
                connect[j] = 0
    
    return sum(connect)

def solution2(n, results):
    answer = 0
    win, lose = defaultdict(set), defaultdict(set)
    for result in results:
            lose[result[1]].add(result[0])
            win[result[0]].add(result[1])

    print("win : ",win)
    print("lose : ",lose)

    for i in range(1, n + 1):
        for winner in lose[i]:
            win[winner].update(win[i])
        for loser in win[i]:
            lose[loser].update(lose[i])

    print("win : ",win)
    print("lose : ",lose)

    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n - 1: answer += 1
    return answer


solution2(n, results)

