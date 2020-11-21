#  Z

'''
메모리초과.. 답 봐도 모르겠음.
'''
N, r, c = map(int, input().split())

z_map = [[0 for i in range(2**N)] for j in range(2**N)]

count = 0


def solve(N, x, y):
    global count
    if N == 1:
        z_map[x][y] = count
        count += 1
        z_map[x][y+1] = count
        count += 1
        z_map[x+1][y] = count
        count += 1
        z_map[x+1][y+1] = count
        count += 1
        return
    n = N-1

    for i in range(2):
        for j in range(2):
            solve(n, x+(i*2**n), y+(j*2**n))


solve(N, 0, 0)
print(z_map[r][c])
