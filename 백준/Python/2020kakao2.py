#orders 배열을 돌면서 course에 있는 수대로 조합을 만듬
#조합을 저장하는 배열을 따로 만듬
#배열을에 조합배열 내용물을 하나씩 꺼내서 2개이상인지 조사
#2개이상이면 result 배열에 넣어줌.


orders=["XYZ", "XWY", "WXA"]
course=[2,3,4]
result=[]
from itertools import combinations


for n in course:
    array=[]
    for i in orders:
        for j in combinations(i , n):
            joinstr=''.join(j)
            if joinstr not in array:
                array.append(joinstr)
    print(array)
    countlist=[]
    for z in array:
        arraylist=list(z)
        count=0
        for j in orders:
            orderslist=list(j)
            c=True
            for t in arraylist:
                if t not in orderslist:
                    c=False
                    break
            if c:
                count+=1
        countlist.append([count,z])
    if len(countlist)>=1:
        maxCount=max(countlist)[0]
        for i in countlist:
            if maxCount>=2 and maxCount == i[0]:
                result.append(i)
print(result)

answer=[]
for i in result:
    k=i[1]
    k=''.join(sorted(k))
    if k not in answer:
        answer.append(k)
answer=sorted(answer)
print(answer)



#맞음
