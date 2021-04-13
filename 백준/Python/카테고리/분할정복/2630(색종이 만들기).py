'''
풀이
분할정복
'''
# import sys
# input = sys.stdin.readline

# N = int(input())
# mat = [list(map(int,input().split())) for i in range(N)]

# blue = 0
# white = 0


# def is_all(m,n):
#     color = m[0][0]
#     for i in range(n):
#         for j in range(n):
#             if m[i][j] != color:
#                 return False
#     return True

# #k 사분면 으로 쪼갠 mat 리턴
# def divide(mat,n,k): 
#     temp=[]
#     if k==1:
#         for i in range(n):
#             temp.append(mat[i][:n])
#         return temp
#     if k==2:
#         for i in range(n):
#             temp.append(mat[i][n:])
#         return temp
#     if k==3:
#         for i in range(n):
#             temp.append(mat[i+n][:n])
#         return temp
#     if k==4:
#         for i in range(n):
#             temp.append(mat[i+n][n:])
#         return temp


# def f(mat,n):
#     global blue, white
#     #마지막 1장일때
#     if n == 1:
#         if mat[0][0] == 1: #파란색
#             blue+=1
#             return
#         else: #흰색
#             white+=1
#             return
#     #1장이 아닌데 모두 색이 같을 경우
#     if is_all(mat,n):
#         color = mat[0][0]
#         if color: #파란색
#             blue+=1
#             return
#         else:
#             white+=1
#             return
#     # 모두 같지 않으니 4등분하기

#     n //=2
#     for i in range(1,5):
#         f(divide(mat,n,i),n)

# f(mat,N)
# print(white)
# print(blue)

            

import sys
matrix = []
white = 0
blue = 0


def check(start_row, end_row, start_col, end_col):
    print("start_row, end_row, start_col, end_col",start_row, end_row, start_col, end_col)
    global blue, white

    if start_row == end_row - 1 and start_col == end_col - 1:
        if matrix[start_row][start_col] == '1':
            blue += 1
        else:
            white += 1
        return

    tmp = matrix[start_row][start_col]
    for i in range(start_row, end_row):
        for j in range(start_col, end_col):
            if tmp != matrix[i][j]:
                check(start_row, (start_row+end_row)//2, start_col, (start_col+end_col)//2)
                check((start_row+end_row)//2, end_row, start_col, (start_col+end_col)//2)
                check(start_row, (start_row+end_row)//2, (start_col+end_col)//2, end_col)
                check((start_row+end_row)//2, end_row, (start_col+end_col)//2, end_col)
                return

    if tmp == '1':
        blue += 1
    else:
        white += 1
    return


def main():
    global matrix
    num = int(input())
    matrix = [[0] * num for _ in range(num)]

    for i in range(num):
        tmp = sys.stdin.readline().split()
        for j in range(num):
            matrix[i][j] = tmp[j]

    check(0, num, 0, num)
    print(white)
    print(blue)


if __name__ == "__main__":
    main()