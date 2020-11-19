# 종이의 개수

'''
조건이 맞지 않다면 계속 분할
조건이 맞다면 (1개 or 모두 같음) 리턴

#시간복잡도 마스터 이론 적용

①나누어지는 문제의 개수 =a
②분할 후 문제의 크기 =b
③각 문제마다 병합(정복) 단계에서 걸리는 시간 =c

종이의 개수 a=9 b=9 d=1  로 시간복잡도는 마스터 이론에 따라 nlogn 이다.
'''
# from sys import stdin

# input = stdin.readline

N = int(input())
paper = [list(map(int, list(input().split()))) for i in range(N)]

count_minus_one = 0
count_one = 0
count_zero = 0


def cut(paper, N):
    global count_minus_one
    global count_one
    global count_zero
    if N == 1:
        if paper[0][0] == 1:
            count_one += 1
        elif paper[0][0] == -1:
            count_minus_one += 1
        else:
            count_zero += 1
        return

    else:
        num = paper[0][0]
        ch = True
        for i in paper:
            for j in i:
                if j != num:
                    ch = False
                    break
            if not ch:
                break
        if ch:
            if num == 1:
                count_one += 1
            elif num == -1:
                count_minus_one += 1
            else:
                count_zero += 1
            return

    n = N//3
    for i in range(3):
        for j in range(3):
            ret_paper = []
            for k in range(n):
                ret_paper.append(paper[j*n+k][i*n:i*n+n])

            cut(ret_paper, n)


cut(paper, N)
print(count_minus_one)
print(count_zero)
print(count_one)
