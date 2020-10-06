box=[7,5,4,2,2]
crain=[19,8,3]
count=0

import sys
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
    else:
        print(-1)
        sys.exit()

print(count)
