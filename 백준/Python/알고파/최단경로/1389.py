# 케빈 베이컨의 6단계 법칙

# 풀이 과정
'''
각 노드의 모든 최단거리를 찾는거니 플로이드 와샬 알고리즘 사용
1.dist 작성하고
2.플로이드 와샬 알고리즘 적용
3.출력
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dist = [[0 if i == j else sys.maxsize for j in range(N+1)] for i in range(N+1)]

for i in range(M):
    A, B = map(int, input().split())
    dist[A][B] = 1
    dist[B][A] = 1

for k in range(N+1):
    for i in range(N+1):
        for j in range(N+1):
            dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])

array = []
for i in dist[1:]:
    total = sum(i[1:])
    array.append(total)
print(array.index(min(array))+1)
