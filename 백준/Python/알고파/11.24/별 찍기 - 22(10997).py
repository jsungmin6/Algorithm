# 별 찍기 - 22
# 풀이 과정
'''
박스를 먼저 만들고 하는게 맞는듯
정확히 출력해야 해서 띄어쓰기랑 공백을 신경써야 함. 
'''

N = int(input())
c = 1+4*(N-1)
r = 3+4*(N-1)
Map = [[' ']*c for i in range(r)]
Map[(3+4*(N-1))//2][(1+4*(N-1))//2] = '*'
Map[(3+4*(N-1))//2+1][(1+4*(N-1))//2] = '*'

if N == 1:
    print('* ')
    exit()

def star(left,right,top,bottom,Map,N):
    if N == 1:
        return
    for i in range(top,bottom):
        if i == top or i == bottom-1:
            for j in range(left,right):
                Map[i][j] = '*'
        Map[i][left] = '*'
        if i == top+1:
            Map[i][right-1] = ' '
        elif i ==top+2:
            Map[i][right-2] = '*'
            Map[i][right-1] = '*'
            Map[i][right-3] = '*'
        else:
            Map[i][right-1] = '*'
    return star(left+2,right-2,top+2,bottom-2,Map,N-1)

star(0,c,0,r,Map,N)
for i in range(len(Map)):
    if i==1:
        line = '* '
    else:
        line = str(''.join(Map[i])) + ' '
    print(line)