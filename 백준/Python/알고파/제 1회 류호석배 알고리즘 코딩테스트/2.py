# 2번 - 인내의 도미노 장인 호석

# 풀이 과정
'''
천천히 구현 해보면 될 듯?
'''

from copy import deepcopy
import sys
input = sys.stdin.readline

N,M,R = map(int,input().split());
Map = [list(map(int,input().split())) for i in range(N)]
copy_Map = deepcopy(Map)
count = 0

def change_F(Ax,Ay,D):
    global count
    A_Num = copy_Map[Ax][Ay]
    if A_Num == 'F':
        return
    A_Num-=1
    if A_Num == 0:
        if copy_Map[Ax][Ay] != 'F':
            copy_Map[Ax][Ay] = 'F'
            count+=1
    if D == 'E':
        for i in range(A_Num):
            if copy_Map[Ax][Ay] != 'F':
                copy_Map[Ax][Ay] = 'F'
                count+=1
            Ay+=1
            if Ay >= M:
                break
            else:
                change_F(Ax,Ay,D)
    elif D == 'W':
        for i in range(A_Num):
            if copy_Map[Ax][Ay] != 'F':
                copy_Map[Ax][Ay] = 'F'
                count+=1
            Ay-=1
            if Ay < 0:
                break
            else:
                change_F(Ax,Ay,D)
    elif D == 'S':
        for i in range(A_Num):
            if copy_Map[Ax][Ay] != 'F':
                copy_Map[Ax][Ay] = 'F'
                count+=1
            Ax+=1
            if Ax >= N:
                break
            else:
                change_F(Ax,Ay,D)
    else:
        for i in range(A_Num):
            if copy_Map[Ax][Ay] != 'F':
                copy_Map[Ax][Ay] = 'F'
                count+=1
            Ax-=1
            if Ax < 0:
                break
            else:
                change_F(Ax,Ay,D)

for _ in range(R):
    Ax,Ay,D = input().split()
    Ax=int(Ax)-1
    Ay=int(Ay)-1
    Dx,Dy = map(int,input().split())
    Dx-=1
    Dy-=1

    A_Num = copy_Map[Ax][Ay]
    if A_Num == 'F':
        continue

    change_F(Ax,Ay,D)

    
    D_Num = copy_Map[Dx][Dy]
    if D_Num != 'F':
        continue
    else:
        copy_Map[Dx][Dy] = Map[Dx][Dy]
    

for i in range(N):
    for j in range(M):
        if copy_Map[i][j] != 'F':
            copy_Map[i][j] = 'S'

print(count)
for i in copy_Map:
    for j in i:
        print(j, end=' ')
    print()


