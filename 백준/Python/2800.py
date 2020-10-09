#괄호 제거

#풀이과정

#비트마스킹으로 못 풀겠어서 결국 인터넷 검색
#'('')'의 짝을 인덱스로 가지는 배열을 만듬(enumerate 활용)
#입력받은 값에서 () 를 다 없앰
#인덱스 배열을 combinaitons 해서 가능한 조합을 배열에 삽입
#정렬

######################

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
