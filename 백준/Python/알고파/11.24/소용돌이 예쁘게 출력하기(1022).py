# 풀이 방법

'''
소욜돌이 배열 만들고 범위만큼 잘라서 출력하는 문제.
1.어느정도 크기로 배열을 만들어야 하는가 -> 절대값이 큰 r1,c2,r2,c2가 결정
2.맵을 만들고 로직을 만들어 내용물을 채워놓고 범위만큼 자른다.
'''

r1, c1, r2, c2 = map(int, input().split())
max_n = max(abs(r1), abs(r2), abs(c1), abs(c2))

Map = [[0 for i in range(max_n*2+1)] for j in range(max_n*2+1)]

Map[max_n][max_n] = '1'


def solution(N, max_n, Map, count):
    if N == max_n+1:
        return

    for i in range(0, N*2):
        Map[max_n+N-1-i][max_n+N] = str(count)
        count += 1

    for i in range(0, N*2):
        Map[max_n-N][max_n+N-1-i] = str(count)
        count += 1

    for i in range(0, N*2):
        Map[max_n-N+1+i][max_n-N] = str(count)
        count += 1

    for i in range(0, N*2):
        Map[max_n+N][max_n-N+1+i] = str(count)
        count += 1

    return solution(N+1, max_n, Map, count)


solution(1, max_n, Map, 2)
for i in range(r1+max_n, r2+max_n+1):
    print(' '.join(Map[i][(c1+max_n):(c2+max_n+1)]))
