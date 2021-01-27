'''
내용
table[i][j] = i-1번째 의 나머지 2색중 작은 거 + 현재 자신의 색 점수

시간복잡도

블로그 이해 필요 : https://blog.naver.com/kks227/220793134705

'''



N=int(input())
homes =[list(map(int,input().split())) for _ in range(N)]
table = [[-1 for _ in range(3)] for _ in range(N)]

for i in range(N):
    for j in range(3):
        if i == 0 :
            table[i][j] = homes[i][j]
        else:
            table[i][j] = min(table[i-1][(j+1)%3],table[i-1][(j+2)%3]) + homes[i][j]

print(min(table[-1]))

