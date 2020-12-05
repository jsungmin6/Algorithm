import sys
input = sys.stdin.readline

T=int(input())
for _ in range(T):
    N = int(input())
    trees = list(map(int,input().split()))
    trees.sort()
    new_A=[]
    new_B=[]
    answer = 0

    for i in range(N):
        if i%2 == 0:
            new_A.append(trees[i])
        else:
            new_B.append(trees[i])
    
    new_B=new_B[::-1]
    new_A.extend(new_B)

    for i in range(len(new_A)):
        answer = max(answer,abs(new_A[i]-new_A[i-1]))

    print(answer)

