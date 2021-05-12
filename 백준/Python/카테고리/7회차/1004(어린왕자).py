'''
풀이

시작점과 도착점 두 좌표가 원안에 포함되는 수를 센다.
시작점 or 도착점 둘 중 하나만 포함되는 경우는 cnt+=1
둘다 포함되거나 둘다 포함 안될때는 아무일도 안 일어난다.
cnt가 답이다.

포함하는지 여부는 원을 중심으로 거리를 측정해서 반지름 안에 들어가는지 체크

'''
import sys
import math
from collections import deque
input = sys.stdin.readline

T = int(input())

def is_in(p,x,y):
    cx,cy,r = p
    len_x = abs(x-cx)
    len_y = abs(y-cy)


    rg = math.sqrt(len_x**2 + len_y**2)

    if rg <= r:
        return True
    return False


def min_in_out(sx,sy,es,ey,planets):
    cnt = 0

    for p in planets:
        if is_in(p,sx,sy) and not is_in(p,es,ey):
            cnt+=1
        elif not is_in(p,sx,sy) and is_in(p,es,ey):
            cnt+=1
    return cnt


for _ in range(T):
    sx,sy,es,ey = map(int,input().split())
    n = int(input())
    planets = [list(map(int,input().split())) for i in range(n)]

    answer = min_in_out(sx,sy,es,ey,planets)
    print(answer)


