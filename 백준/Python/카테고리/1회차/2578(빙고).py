'''
풀이
구현
'''

def bingo(mat):
    cnt=0
    for row in mat:
        if sum(row) == 0:
            cnt+=1
    for i in range(5):
        if mat[0][i]+mat[1][i]+mat[2][i]+mat[3][i]+mat[4][i] == 0:
            cnt+=1
    if mat[0][0]+mat[1][1]+mat[2][2]+mat[3][3]+mat[4][4] == 0:
        cnt+=1
    if mat[0][4]+mat[1][3]+mat[2][2]+mat[3][1]+mat[4][0] == 0:
        cnt+=1
    if cnt >= 3:
        return True
    else:
        return False

def choice(mat,target):
    for r in range(5):
        if target in mat[r]:
            mat[r][mat[r].index(target)] = 0
            return


import sys
input = sys.stdin.readline


mat = [list(map(int,input().split())) for i in range(5)]
cnt = 0


nums = []

for i in range(5):
    data = list(map(int,input().split()))
    for d in data:
        nums.append(d)

for j in nums:
    cnt+=1
    choice(mat,j)

    if bingo(mat):
        print(cnt)
        break





