

from itertools import combinations
problem = [*input().strip()] # 문자열 하나씩 리스트화

p, idx_brs = [],[]
# 짝이 맞는 괄호의 위치 idx_brs에 저장해줌
for i,v in enumerate(problem):
    if v == '(':
        problem[i] =''
        p+=[i]
    if v == ')':
        problem[i] ='';
        idx_brs +=[[p.pop(),i]]

out = set()

# 짝이 맞는 괄호 위치를 조합을 통해 조정해줌
for i in range(len(idx_brs)):
    for j in combinations(idx_brs,i):
        P = problem[:]
        for v,w in j:
            P[v] = '('
            P[w] = ')'
        out.add(''.join(P))
for i in sorted(out):print(i)
