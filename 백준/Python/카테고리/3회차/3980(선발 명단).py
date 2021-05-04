'''
풀이
S의 ij는 i번 선수가 j번 포지션에서 뛸 떄의 능력이다

이미 방문한 포지션을 제외하고 자신이 뛸 수 있는 포지션들을 재귀적으로 호출한다.
visited에 이미 선택된 포지션을 체크하고 백트래킹 기법을 사용해 모든 경우를 탐색한다.

함수의 매개변수는 (맵, 선택한 인원, 능력치합, 방문체크)
'''

import sys
input = sys.stdin.readline

def f(mat,n,sum,vistied):
    if n == 11:
        return sum
    answer = 0
    for i in range(11): #n번째 선수의 뛸 수 있는 포지션
        if mat[n][i] != 0 and not visited[i]:
            visited[i] = 1
            answer = max(f(mat,n+1,sum+mat[n][i],visited),answer)
            visited[i] = 0
    
    return answer

T = int(input())
for _ in range(T):
    mat = [list(map(int,input().split())) for i in range(11)]
    visited = [0]*11

    answer = f(mat,0,0,visited)

    print(answer)