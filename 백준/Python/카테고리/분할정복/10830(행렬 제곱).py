'''
풀이
행렬제곱
'''
def productMatrix(arr1, arr2):
    answer = []
    for idx1 in range(len(arr1)):
        row = []
        for idx2 in range(len(arr2[0])):
            tmp = 0
            for idx3 in range(len(arr1[0])):
                tmp += arr1[idx1][idx3] % 1000 * arr2[idx3][idx2] % 1000
                tmp = tmp % 1000
            row.append(tmp)
        answer.append(row)
    return answer


N,B = map(int,input().split())
matrix = [list(map(lambda x: x % 1000, map(int,input().split()))) for i in range(N)]

def solve(tmp_b):
    global matrix
    if(tmp_b == 1):
        return matrix
    t = solve(int(tmp_b/2))
    t = productMatrix(t, t)
    if(tmp_b % 2 != 0):
        t = productMatrix(t, matrix)
    return t

for m in solve(B):
    print(" ".join(map(str, m)))



