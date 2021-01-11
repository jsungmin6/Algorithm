import sys
from itertools import permutations

N,M = map(int,input().split())
DNAs = []
for _ in range(N):
    DNAs.append(input().rstrip())

S=['A','C','G','T']
result_DNA = []
diff=0
for i in range(M):
    temp=[]
    max_c=0
    ans=''
    for dna in DNAs:
        temp.append(dna[i])

    for s in S:
        c = temp.count(s)
        if c > max_c:
            max_c = c
            ans=s
    
    for dna in DNAs:
        if dna[i] != ans:
            diff+=1

    result_DNA.append(ans)

print(''.join(result_DNA))
print(diff)

