'''
그룹별로 다른 수를 부여해서 구분할 수 있도록 하고
첫번째그룹 앞에 두번째그룹이 있다면 자리를 바꿀 수 있도록 함
'''

N1, N2 = map(int, input().split())
G = []
for i in list(input())[::-1]:
    G.append([1, i])

for i in list(input()):
    G.append([2, i])
T = int(input())
for _ in range(T):
    temp=[]
    for i in range(N1+N2-1):
        if G[i][0] == 1 and G[i+1][0] == 2:
            temp.append(i)
    
    for i in temp:
        G[i],G[i+1] = G[i+1],G[i]

for i in G:
    print(i[1], end='')
