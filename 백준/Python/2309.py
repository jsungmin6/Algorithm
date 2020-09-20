#일곱 난쟁이 B2

#풀이 계획

#모든 경우를 모두 찾음
#만약 합이 100이 되면 정렬
#출력

###################################

from itertools import combinations

array=[]

for _ in range(9):
    array.append(int(input()))

for i in combinations(array,7):
    if sum(i) == 100:
        k=list(i)
        k.sort()
        for j in k:
            print(j)
        break

#다른풀이
A = [] for i in range(9):
A.append(int(input()))
A.sort() result = sum(A)
for i in range(9) :
    for j in range(i+1,9):
        if result-A[i]-A[j]==100:
            for k in range(9) :
                if k == i or k == j:
                    continue
                else :
                    print(A[k]) exit()
