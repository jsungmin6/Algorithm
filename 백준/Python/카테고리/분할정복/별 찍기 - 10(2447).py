#  별 찍기 - 10

'''

'''
N = int(input())

Map = [[' ' for i in range(N)] for j in range(N)]


def star(N, x, y):
    if N == 3:
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    Map[x+i][y+j] = ' '
                else:
                    Map[x+i][y+j] = '*'

        return
    N //= 3
    
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            star(N, x+i*N, y+j*N)


star(N, 0, 0)
for i in Map:
    print(''.join(i))