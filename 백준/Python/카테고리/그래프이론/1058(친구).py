'''
풀이
플로이드 와샬 알고리즘을통해 각각의 최단거리를 모두 구한 후 2 이하인 수를 구한다.
'''

n= int(input())
INF = 987654321

#전처리
dist = []
for _ in range(n):
    temp = []
    row = list(input())
    for i in row:
        if i == "N":
            temp.append(INF)
        else:
            temp.append(1)
    dist.append(temp)

for i in range(n):
    dist[i][i] = 0

#플로이드 와샬
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i==j:
                dist[i][j] = 0
            else:
                dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j])

#거리가 2이하인 수가 제일 많은 행 뽑기
answer = 0
for row in dist:
    cnt = 0
    for c in row:
        if c <= 2 and c != 0:
            cnt+=1
    answer = max(answer,cnt)

print(answer)