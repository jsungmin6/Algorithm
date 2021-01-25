N,new_score,P = map(int,input().split())

if N==0:
    print(1)
    exit(0)

ranks = list(map(int,input().split()))

if new_score<=min(ranks) and len(ranks) >= P:
    print(-1)
    exit(0)

ranks.sort(reverse=True)

count=1

for rank in ranks:
    if rank>new_score:
        count+=1

print(count)