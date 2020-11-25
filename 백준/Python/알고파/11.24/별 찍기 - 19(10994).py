# 별 찍기 - 19 
# 풀이 과정
'''
박스를 먼저 만들고 하는게 맞는듯
정확히 출력해야 해서 띄어쓰기랑 공백을 신경써야 함. 
'''

N = int(input())
r = 1+4*(N-1)
c = 1+4*(N-1)
Map = [[' ']*c for i in range(r)]





def star(left,right,top,bottom,Map):
    # 조건 리턴
    if left == right:
        Map[top][left] = '*'
        return
    # 그리기
    for i in range(top,bottom):
        if i == top or i == bottom-1:
            for j in range(left,right+1):
                Map[i][j] = '*'
        Map[i][left] = '*'
        Map[i][right] = '*'
    return star(left+2,right-2,top+2,bottom-2,Map)

star(0,c-1,0,r,Map)


for i in Map:
    line = str(''.join(i)) + ' '
    print(line)
