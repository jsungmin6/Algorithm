#  쿼드트리

'''
조건이 맞지 않다면 계속 분할
조건이 맞다면 (1개 or 모두 같음) 리턴

'''
import sys
input = sys.stdin.readline
N = int(input())
Map = [list(map(int, list(input().rstrip()))) for i in range(N)]
answer = ""


def check(map, N):
    type = map[0][0]
    if N == 1:
        return True

    for i in range(N):
        for j in range(N):
            if map[i][j] != type:
                return False
    return True


def tree(Map, N):
    global answer
    # for i in Map:
    # print(i)
    if check(Map, N):
        s = str(Map[0][0])
        answer = answer+s
        # print('answer : ', answer)
        return
    answer = answer+"("
    n = N//2
    for i in range(2):
        for j in range(2):
            ret_map = []
            for k in range(n):
                ret_map.append(Map[i*n+k][j*n:j*n+n])

            tree(ret_map, n)
    answer = answer+")"


tree(Map, N)
print(answer)

# 다른사람 풀이

t = int(sys.stdin.readline())
l = []
for o in range(t):
    l.append([int(c) for c in sys.stdin.readline().rstrip()])



def dc(x, y, n):
    if n == 1:
        return str(l[y][x])
    t = [l[i][x: x+n] for i in range(y, y + n)]
    c = t[0][0]
    if t[0].count(c) == n:
        if t.count(t[0]) == n:
            return str(c)

    n //= 2
    return "(" + dc(x, y, n) + dc(x + n, y, n) + dc(x, y + n, n) + dc(x + n, y + n, n) + ")"


print(dc(0, 0, t))



# BOJ 1992 - 쿼드 트리 - 분할 정복
import sys
r = sys.stdin.readline


def decompose(n, y, x):
    # print(n, y, x)
    if n == 1:
        print(image[y][x], end="")
        return

    flag = True
    for i in range(y, y+n):
        if not flag:
            break
        for j in range(x, x+n):
            if image[i][j] != image[y][x]:
                flag = False
                break

    if flag:
        print(image[y][x], end="")
    else:
        decreased_n = n//2

        print("(", end="")
        decompose(decreased_n, y, x)
        decompose(decreased_n, y, x+decreased_n)
        decompose(decreased_n, y+decreased_n, x)
        decompose(decreased_n, y+decreased_n, x+decreased_n)
        print(")", end="")


N = int(r())
image = [list(r().strip()) for _ in range(N)]
decompose(N, 0, 0)