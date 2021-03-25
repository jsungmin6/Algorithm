'''
'''
T=int(input())
for _ in range(T):
    n=int(input())
    coins=list(map(int,input().split()))
    m=int(input())

    array=[[0]*(m+1) for _ in range(n+1)]

    for i in range(1,n+1):
        w,v = map(int,input().split())
        for j in range(1,m+1):
            if j<w:
                array[i][j]=array[i-1][j]
            else:
                array[i][j]=max(array[i-1][j],array[i-1][j-w]+v)

    print(array[n][m])

'''
array[i][j] 물먹을 i 개 받았고 최대무게가 j일때 가치의 최댓값
'''
n,m=map(int,input().split())

