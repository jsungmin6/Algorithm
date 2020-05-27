import sys

n=int(input())
crain=list(map(int,input().split()))
crain.sort(reverse=True)

m=int(input())
box=list(map(int,input().split()))
box.sort(reverse=True)

if max(crain) < max(boxes):
    print(-1)
    sys.exit()

index=-1
for w in range(len(box)):
    if index==0:
        count+=1
    index+=1
    while True:
        index%=3
        if crain[index]>=box[w]:
            crain[index]-=box[w]
            break
        else:
            index+=1

print(count)
