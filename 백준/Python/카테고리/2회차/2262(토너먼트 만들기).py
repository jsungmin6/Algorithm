'''
풀이

붙는 선수끼리의 랭킹차이가 적어야 한다.
이기는 선수(여러번 붙는 선수)는 랭킹이 높은 선수이다.
따라서 랭킹이 올라가서 여러번 붙으면 안된다. 올라가는 선수들은 랭킹이 높은 선수들이기 때문에 차이값이 많아진다.
즉 랭킹이 낮은 선수부터 시합을 뛰게해 제거한다.

랭킹이 제일 낮은 선수를 찾고 양 옆의 선수중 차이가 적은 선수랑 붙는다.
그리고 랭킹이 낮은 선수를 제거한다.
1명이 남을 때까지 반복한다.
'''

n = int(input())
ranks = list(map(int,input().split()))
answer = 0
while len(ranks) !=1:
    rank = max(ranks)
    idx = ranks.index(rank)
    diff = 0

    if idx == 0:
        diff = rank - ranks[1]
    elif idx == len(ranks)-1:
        diff = rank - ranks[idx-1]
    else:
        diff = min(rank - ranks[idx-1],rank - ranks[idx+1])
    answer+=diff
    del ranks[idx]

print(answer)
