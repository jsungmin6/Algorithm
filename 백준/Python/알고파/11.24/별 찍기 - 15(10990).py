#별찍기 - 15

# 풀이 과정
'''
for문 2개로 수열 생각하면서 규칙 찾기
'''
N= int(input())
left = N-1
right = N-1
for i in range(N,2*N):
    for j in range(i):
        if j==left or j==right:
            print('*',end="")
        else:
            print(' ',end="")
    left-=1
    right+=1
    print()
