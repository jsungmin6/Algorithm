#분해합 B2

#풀이 계획

#생성자는 N보다 작다.
#N 이하의 모든 수의 생성자를 구해보고 N이 되는 경우를 찾아보자

###################################

N=int(input())
answer=0
for i in range(N):
    answer+=i
    strI=str(i)
    for j in strI:
        answer+=int(j)
    if answer==N:
        print(i)
        break
    else:
        answer=0
else:
    print(0)
