#info 정보를 2차원배열로 저장한다.
#query 를 for 문으로 하나씩 불러와 파싱하고 조건이 맞는 데이터 가있는지 검색.
#숫자표시

info=["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query=["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

data=[[] for i in range(len(info))]
for i in range(len(info)):
    type, kind, age, food, score=info[i].split(' ')
    data[i].append(type)
    data[i].append(kind)
    data[i].append(age)
    data[i].append(food)
    data[i].append(score)
result=[]
for text in query:
    text=text.replace("and","")
    type, kind, age, food, score=text.split()

    count=0
    for i in data:
        box=[0]*5
        if type=='-' or type==i[0]:
            box[0]=1
        else:
            continue
        if kind=='-' or kind==i[1]:
            box[1]=1
        else:
            continue
        if age=='-' or age==i[2]:
            box[2]=1
        else:
            continue
        if food=='-' or food==i[3]:
            box[3]=1
        else:
            continue
        if score=='-' or int(score)<=int(i[4]):
            box[4]=1
        else:
            continue
        count+=1
    result.append(count)
print(result)


#효율성 탈락
